import os
from sqlalchemy import create_engine

class SourceConnector:
    def __init__(self):
        self.source_db = os.getenv('SOURCE_DB')
        self.engine = None

    def connect(self):
        if self.source_db:
            self.engine = create_engine(self.source_db)
            print("Connection to source database established.")
        else:
            print("SOURCE_DB variable not set.")

    def get_engine(self):
        if self.engine:
            return self.engine
        else:
            return None