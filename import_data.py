import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

source_db = os.getenv('SOURCE_DB_LOCAL')

engine = create_engine(source_db)

chunksize = 10000
chunk_number = 0

for chunk in pd.read_csv('data/Crimes_-_2001_to_Present.csv', chunksize=chunksize):
    chunk.to_sql('chicago_crime', engine, if_exists='append', index=False)
    chunk_number += 1
    print(f"Chunk {chunk_number} imported successfully!")