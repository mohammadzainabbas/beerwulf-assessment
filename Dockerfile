# Stage 1: Builder - Build ETL process and generate star_schema.db
FROM python:3.13-slim AS builder

# Install uv from the prebuilt image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy project configuration files
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies with caching enabled
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Copy application directories (using COPY for better clarity)
COPY data/ data/
COPY etl/ etl/
COPY sql/ sql/

# Execute the ETL process to generate the star_schema.db file
RUN uv run -- python etl/main.py

# Stage 2: Runtime - Minimal image with SQLite installed
FROM alpine:3.21.3 AS runtime

# Install SQLite
RUN apk add --no-cache sqlite

# Set working directory
WORKDIR /app

# Copy generated database and SQL files from the builder stage
COPY --from=builder /app/star_schema.db .
COPY --from=builder /app/sql/ sql/

# When the container starts, launch SQLite on star_schema.db
ENTRYPOINT ["sqlite3"]
CMD ["star_schema.db"]
