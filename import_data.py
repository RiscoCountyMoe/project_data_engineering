import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost/source_database')

chunksize = 10000
chunk_number = 0

for chunk in pd.read_csv('data/Crimes_-_2001_to_Present.csv', chunksize=chunksize):
    chunk.to_sql('chicago_crime', engine, if_exists='append', index=False)
    chunk_number += 1
    print(f"Chunk {chunk_number} imported successfully")