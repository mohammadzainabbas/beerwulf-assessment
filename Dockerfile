# Stage 1: Builder - Run the ETL process to generate "star_schema.db"
FROM ghcr.io/astral-sh/uv:0.6 as builder

# Change the working directory to the `app` directory
WORKDIR /app

# Copy the pyproject.toml file
COPY pyproject.toml .

# Install dependencies
RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml uv sync

# Copy the "data", "etl" directories
COPY data/ etl/ ./

# Run the ETL process
RUN uv run -- python etl/main.py

# Stage 2: Runtime
FROM alpine/sqlite:3.48.0 as runtime

# Change the working directory to the `app` directory
WORKDIR /app

# Copy the generated database and SQL files from the builder stage
COPY --from=builder /app/star_schema.db .
COPY --from=builder /app/sql/ ./sql/

# When the container starts, launch SQLite on star_schema.db
CMD ["sqlite3", "star_schema.db"]