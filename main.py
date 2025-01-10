import os
from application.etl_processor import EtlProcessor

def main():
    etl_processor = EtlProcessor()
    df = etl_processor.extract()
    print(df['ID'])

if __name__ == "__main__":
    main()