
# Database Creation Using Postgresql

# Database Connection
import psycopg2
# conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Opened database successfully')
#
# # Create a table
#
# cur=conn.cursor()
# cur.execute('CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,'
#             'ADDRESS CHAR(50),SALARY REAL);')
# print('Table created successfully')
# conn.commit()
# conn.close()

# INSERT into table

# conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Opened database successfully')
# cur=conn.cursor()
# cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'Paul',32,'California',20000.00)");
# cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'Allen',25,'Texas',15000.00)");
# cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,'Teddy',23,'Norway',20000.00)");
# cur.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(4,'Mark',25,'RichMond',65000.00)");
# conn.commit()
# print('Records created successfully')
# conn.close()


# Select option

# conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Opened database successfully')
# cur=conn.cursor()
# cur.execute("SELECT id,name,address,salary from COMPANY")
# rows=cur.fetchall()
# for row in rows:
#     print("ID=",row[0])
#     print("NAME=",row[1])
#     print("ADDRESS=",row[2])
#     print("SALARY=",row[3])
# print("Operation done successfully")
# conn.close()

# UPDATE OPERATION

# conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Opened database successfully')
# cur=conn.cursor()
# cur.execute("UPDATE COMPANY set SALARY=25000.00 where ID=1")
# conn.commit()
# print("Total number of rows updated:",cur.rowcount)
# cur.execute('SELECT id,name,address,salary from COMPANY')
# rows=cur.fetchall()
# for row in rows:
#     print("ID=",row[0])
#     print("NAME=",row[1])
#     print("ADDRESS=",row[2])
#     print("SALARY=",row[3])
# print("Operation done successfully")
# conn.close()

# Delete Operation

conn=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
print('Opened database successfully')
cur=conn.cursor()
cur.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print("Total number of rows deleted:",cur.rowcount)
cur.execute('SELECT id,name,address,salary from COMPANY')
rows=cur.fetchall()
for row in rows:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3])
print("Operation done successfully")
conn.close()


