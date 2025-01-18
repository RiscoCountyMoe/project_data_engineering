import os
from application.etl_processor import EtlProcessor

def main():
    partition_cols = ['Year', 'District', 'Primary Type']
    chunk_size = 100000

    etl_processor = EtlProcessor()
    etl_processor.process_in_chunks(chunk_size, partition_cols)

if __name__ == "__main__":
    main()