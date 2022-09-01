import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#connection details and password hidden in virtual environmrnt

engine = create_engine(pg_url, pool_recycle=-1)

print('Engine created successfully')

# #Load Csv file into postgresql from python using the to_sql() function
# df = pd.read_csv("studentsscore.csv")

# df.to_sql('students', con=engine, if_exists='append', index=False)

# print("Done")