.PHONY: prepare start plugins migration show

prepare:
	python import_data.py

start:
	docker exec -it etl python /app/main.py

plugins:
	docker exec -it metabase chmod -R 777 /plugins

migration:
	docker exec -it trino trino --execute "CREATE SCHEMA IF NOT EXISTS minio.data WITH (location = 's3a://data/'); \
	CREATE TABLE IF NOT EXISTS minio.data.dataset (Date VARCHAR, Block VARCHAR, Primary_Type VARCHAR, Location_Description VARCHAR, \
	Arrest BOOLEAN, Domestic BOOLEAN, Beat INT, Ward DOUBLE, Community_Area DOUBLE, Year INT) WITH (external_location = 's3a://data/', \
	format = 'PARQUET');"
show:
	docker exec -it trino trino --execute "SHOW TABLES IN minio.data; SELECT * FROM minio.data.dataset LIMIT 5;"