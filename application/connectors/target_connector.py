import os
from sqlalchemy import create_engine

class TargetConnector:
    def __init__(self):
        self.source_db = os.getenv('')
        self.engine = None

    def connect(self):
        pass

    def get_engine(self):
        if self.engine:
            return self.engine
        else:
            return None