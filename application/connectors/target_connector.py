import os
from minio import Minio
from minio.error import S3Error

class TargetConnector:
    def __init__(self):
        self.client = None
        self.target_db = os.getenv('MINIO_DB')
        self.bucket = os.getenv('MINIO_DEFAULT_BUCKETSS')
        self.user = os.getenv('MINIO_ROOT_USER')
        self.password = os.getenv('MINIO_ROOT_PASSWORD')

    def connect(self):
        if self.target_db and self.user and self.password:
            self.client = Minio(self.target_db, self.user, self.password, secure=False)
            print("Connection to MinIO established.")
        else:
            print("MinIO environment variables not set.")


    def get_client(self):
        if self.client:
            return self.client
        else:
            return None