import os
from application.etl_processor import EtlProcessor

def main():
    chunk_size = 100000

    etl_processor = EtlProcessor()
    etl_processor.process_in_chunks(chunk_size)

if __name__ == "__main__":
    main()