# Project Setup

## Steps to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RiscoCountyMoe/project_data_engineering.git
    ```
2. **Create a folder**:
    Create a folder named `data` in your project directory.
3. **Download the dataset**:
    Download the dataset from this link (https://1drv.ms/x/c/7692cb1e67a6dc27/Ea1kpkC4tfZEhqG5nXdjXGgBqTDkyqzpg4NltIlswA5pfg?e=L0XxjG&download=1) and add it to your `data` folder.
4. **Build the containers**:
    ```bash
    docker compose build
    ```
5. **Start the containers**:
    ```bash
    docker compose up -d
    ```
6. **Import data**:
    ```bash
    make prepare
    ```
    This marks the starting point for the ETL pipeline.
7. **Run the pipeline**:
    ```bash
    make start
    ```
    - If plugins in Metabase cannot be installed, run:
    ```bash
    make plugins
    ```
8. **Create schema and table in Trino**:
    ```bash
    make migration
    ```
9. **Set up Metabase**:
    Open http://localhost:9000 and create your own Metabase.
    - To add a database, use the Presto or Starburst driver:
        - Host: trino
        - Port: 8080
        - Catalog: minio
        - Schema: data
        - Username: user
        - Password: leave empty (Trino does not allow passwords)

    You can now explore the data in Metabase and create simple dashboards.
