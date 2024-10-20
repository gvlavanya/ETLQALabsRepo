from pymysql import connect
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+pymysql://root:Mysql_123@localhost:3306/etlAutomation')
connection = engine.connect()

query="select * from employees"
df_target = pd.read_sql(query,connection)
print (df_target)
