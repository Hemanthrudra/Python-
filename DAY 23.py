
# ETL Project
# Using CSV,EXCEL and JSON file

import pandas as pd
df_xl=pd.read_excel("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/ExcelETL.xlsx")
print(df_xl)

df_json=pd.read_json("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/sample3.json")
print(df_json)

df_csv=pd.read_csv("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/CSVETL.csv")
print(df_csv)

df_all=pd.concat([df_xl,df_json,df_csv],axis=0)
print(df_all)
df_all.sort_values(by='ID',inplace=True)
print(df_all)

import psycopg2
conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
print('Opened database successfully')
cur=conn.cursor()
# cur.execute('CREATE TABLE TEST(ID INT NOT NULL,NAME TEXT NOT NULL)')
# print('Table created successfully')
cur.execute('DROP TABLE TEST')
# conn.close()
# cur.execute()
# from sqlalchemy import create_engine
# engine = create_engine('postgresql://postgres:admin@127.0.0.1:5432/postgres')
# df_all.to_sql('ETL', engine)
conn.commit()