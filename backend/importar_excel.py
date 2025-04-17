import pandas as pd
import sqlite3


df = pd.read_excel('backend/backend/media/Ambientes.xlsx')
print(df.head())

conn = sqlite3.connect('db.sqlite3')

df.to_sql('app_empresa_ambiente', conn, if_exists='append', index=False)

conn.close()
