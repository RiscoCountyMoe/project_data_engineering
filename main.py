import os
from application.etl_processor import EtlProcessor

def main():
    etl_processor = EtlProcessor()
    df = etl_processor.extract()
    print(df['ID'])
    parquet = etl_processor.transform(df)
    etl_processor.load(parquet, 'data.parquet')

if __name__ == "__main__":
    main()