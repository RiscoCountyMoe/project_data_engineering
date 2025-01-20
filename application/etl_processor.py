import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from application.connectors.source_connector import SourceConnector
from application.connectors.target_connector import TargetConnector
from minio.error import S3Error
import multiprocessing as mp


class EtlProcessor:
    def __init__(self):
        self.sorce_connector = SourceConnector()
        self.sorce_connector.connect()
        self.engine = self.sorce_connector.get_engine()
        self.table_name = 'public.chicago_crime'
        self.target_connector = TargetConnector()
        self.target_connector.connect()
        self.client = self.target_connector.get_client()

    def extract(self, offset, chunk_size):
        if self.engine and self.table_name:
            query = f"SELECT * FROM {self.table_name} LIMIT {chunk_size} OFFSET {offset}"
            df = pd.read_sql(query, self.engine)
            return df
        else:
            print("No database connection or table name available.")
            return None
        
    def transform(self, df, partition_cols=None):
        columns_to_drop = ['ID', 'Case Number', 'IUCR', 'Description', 'FBI Code', 'X Coordinate',
              'Y Coordinate', 'Latitude', 'Longitude', 'Updated On', 'Location']
        df = df.drop(columns_to_drop, axis=1)

        if partition_cols:
            pq.write_to_dataset(pa.Table.from_pandas(df), root_path='dataset', partition_cols=partition_cols, compression='brotli')
        else:
            parquet_buffer = io.BytesIO()
            table = pa.Table.from_pandas(df)
            pq.write_table(table, parquet_buffer, compression='brotli')
            parquet_buffer.seek(0)
            return parquet_buffer


    def load(self, file, object_name):
        bucket_name = 'data'
        try:
            self.client.put_object(bucket_name, object_name, file, len(file.getvalue()), content_type='application/csv')
            print(f'{object_name} successfully uploaded to {bucket_name}.')
        except S3Error as e:
            print('An error occured: {e}')

    def process_in_chunks(self, chunk_size, partition_cols=None):
        offset = 0
        while True:
            df = self.extract(offset, chunk_size)
            if df is None or df.empty:
                break
            parquet_buffer = self.transform(df, partition_cols=None)
            if partition_cols:
                object_name = f'dataset/{partition_cols}/{offset}.parquet'
            else:
                object_name = f'{offset}.parquet'
            self.load(parquet_buffer, object_name)
            offset += chunk_size