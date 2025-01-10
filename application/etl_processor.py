import pandas as pd
from application.connectors.source_connector import SourceConnector
from application.connectors.target_connector import TargetConnector

class EtlProcessor:
    def __init__(self):
        self.connector = SourceConnector()
        self.connector.connect()
        self.engine = self.connector.get_engine()
        self.table_name = 'public.chicago_crime'

    def extract(self):
        if self.engine and self.table_name:
            query = f"SELECT * FROM {self.table_name} LIMIT 5"
            df = pd.read_sql(query, self.engine)
            return df
        else:
            print("No database connection or table name available.")
            return None
        
    def transform(self):
        pass

    def load(self):
        pass
