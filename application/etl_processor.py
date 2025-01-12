import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from application.connectors.source_connector import SourceConnector
from application.connectors.target_connector import TargetConnector
from minio.error import S3Error

class EtlProcessor:
    def __init__(self):
        self.sorce_connector = SourceConnector()
        self.sorce_connector.connect()
        self.engine = self.sorce_connector.get_engine()
        self.table_name = 'public.chicago_crime'
        self.target_connector = TargetConnector()
        self.target_connector.connect()
        self.client = self.target_connector.get_client()

    def extract(self):
        if self.engine and self.table_name:
            query = f"SELECT * FROM {self.table_name} LIMIT 5"
            df = pd.read_sql(query, self.engine)
            return df
        else:
            print("No database connection or table name available.")
            return None
        
    def transform(self, df):
        df  = self.extract()
        parquet_buffer = io.BytesIO()
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)
        return parquet_buffer


    def load(self, file, object_name):
        bucket_name = 'data'
        try:
            self.client.put_object(bucket_name, object_name, file, len(file.getvalue()), content_type='application/csv')
            print(f'{object_name} successfully uploaded to {bucket_name}.')
        except S3Error as e:
            print('An error occured: {e}')
