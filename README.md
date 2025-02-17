<div align="center"> 
    <h2> Beerwulf <code>Data Assessment</code> 💻 </h2>
</div>

#

> [!NOTE]
> This mini *ETL* project was done as an assessment for [`Beerwulf`](http://www.beerwulf.com/) for the position of [`Data Engineer (Medior)`](https://beerwulf.homerun.co/data-engineer-medior-2/en). 

<div align="center">

<table>
  <tr>
    <td><strong>CI</strong></td>
    <td>
      <a href="https://github.com/mohammadzainabbas/beerwulf-assessment/actions/workflows/ci.yml">
        <img src="https://github.com/mohammadzainabbas/beerwulf-assessment/actions/workflows/ci.yml/badge.svg" alt="CI">
      </a>
    </td>
  </tr>
  <tr>
    <td><strong>Meta</strong></td>
    <td>
      <a href="https://github.com/astral-sh/uv">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
      </a>
      <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="ruff">
      </a>
      <a href="https://spdx.org/licenses/">
        <img src="https://img.shields.io/badge/license-MIT-9400d3.svg" alt="License - MIT">
      </a>
    </td>
  </tr>
</table>

</div>

#

## Getting Started

### Prerequisites

You need one of the following tools to run this project

- Install [`docker`](https://docs.docker.com/get-docker/)
- Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
- Install [`sqlite3` (optional)](https://www.sqlite.org/download.html)

> [!TIP]
> Install `sqlite3` only if you want to interact with the `star_schema.db` file.

### Clone the repository

```bash
gh repo clone mohammadzainabbas/beerwulf-assessment
cd beerwulf-assessment/
```

or 

```bash
git clone https://github.com/mohammadzainabbas/beerwulf-assessment.git
cd beerwulf-assessment/
```

### Run `ETL` process to generate `star_schema.db` file

Run the following commands to extract, transform and load the data into a star schema model 

```bash
uv sync
uv run -- python etl/main.py
```

or skip all that and run the following command to generate `star_schema.db` via `docker`:

```bash
docker build -t beerwulf-assessment .
```

> [!NOTE]
> Above `docker` command will install all the dependencies, run the [`etl/main.py`](https://github.com/mohammadzainabbas/beerwulf-assessment/blob/main/etl/main.py) script to generate the `star_schema.db` file and invoke the `sqlite3` shell to interact with the database.

### Interact with the `star_schema.db` file (optional)

Once you have the `star_schema.db` file, you can run the following command to interact with the database:

```bash
sqlite3 star_schema.db
```

or with `docker`:

```bash
docker run --rm -it beerwulf-assessment
```

> [!TIP]
> `docker run --rm -it beerwulf-assessment` command will open the `sqlite3` shell with the `star_schema.db` file.


### Query the `star_schema.db` file

1. To get the list of tables:

```sql
sqlite> .tables
```

You should see tables such as `DIM_CUSTOMER`, `DIM_PART`, `DIM_SUPPLIER`, `DIM_DATE`, `FACT_SALES`, `NATION`, and `REGION`.
