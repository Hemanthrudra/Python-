# Assignment
# 1.Age greater than or equal to 18 eligible for vote , not eligible for vote
# 2.Student marks card, marks =44
# Odd or even number.


# 1. Age>=18 eligible
# Using If else statement

# num=18
# if num>=18:
#     print(num,"Eligible for voting")
# else:
#     print(num,"Not Eligile for voting")
#
# num = 15
# if num >= 18:
#      print(num, "Eligible for voting")
# else:
#      print(num, "Not Eligile for voting")

# 2.Student marks=44
# Using if elif statement
#
# num=44
# if num>44:
#     print(num,"Grade B")
# elif num==44:
#     print("Grade c")
# else:
#     print(num,"Fail class")

#
# num=30
# if num>44:
#     print(num,"Grade B")
# elif num==44:
#     print("Grade c")
# else:
#     print(num,"Fail class")

#
# num=35
# if num>=35:
#     print(num,"Pass class")
# elif num==44:
#     print("Grade c")
# else:
#     print(num,"Fail class")


#2. Class 50-60 =Second clas, 60-85=First clas, 85-100-Distinction,<35=Fail
# num=86
# if num>=35:
#     if num>=50 and num<=60:
#         print(num,"Second Class")
#     elif num>60 and num<=85:
#         print(num,"Fisrt class")
#     elif num>85:
#         print(num,"Distinction")
# else:
#     print(num,"Fail")

# 3.Odd even number.

# num=5
# if num%2==0:
#     print(num,"Number is Even")
# else:
#     print(num,"Number is odd")

# 4.Leap year program.

# for i in range(1899,2010):
#     if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
#         print(f"{i} is a leap year")
#     else:
#         print(f"{i} not a leap year")

# Sum 1 to 100

# n=100
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# Armstrong number
# num=153
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
#     if num==sum:
#         print(num,'Is Armstrong number')
#     else:
#         print(num,'Is not armstrong number')

# Armstrong for single number
# num=371
# digits =sum([int(x)**3 for x in str(num)])
# if digits == num:
#     print(f"{digits} is a armstrong Numer")
# else:
#     print(f"{digits} is not a armstrong Numer")

# Armstrong with list
# nums=[371,153,151]
# for num in nums:
#     digits =sum([int(x)**3 for x in str(num)])
#     if digits == num:
#         print(f"{digits} is a armstrong Numer")
#     else:
#         print(f"{digits} is not a armstrong Numer")


# Rock Paper Scissors - Problem

# print("'Please pick one: rock scissors paper'")
# while True:
#     game_dict={'rock':1,'scissors':2,'paper':3}
#     player_a=str(input("Player a:"))
#     player_b=str(input("Player b:"))
#     a=game_dict.get(player_a)
#     b=game_dict.get(player_b)
#     dif=a-b
#
#     if dif in[-1,2]:
#         print('player a wins')
#         if str(input('Do you want to play another game,yes or no?\n'))=='yes':
#             continue
#         else:
#             print('game over.')
#             break
#     elif dif in[-2,1]:
#         print('player b wins.')
#         if str(input('Do you want to play another game,yes or no?\n'))=='yes':
#             continue
#         else:
#             print('game over.')
#             break
#     else:
#         print('Draw.Please continue.')
#         print('')

# import sys
# user1=input("What's your name?")
# user2=input("And your name?")
# user1_answer=input("%s,do you want to choose rock,paper or scissors?"%user1)
# user2_answer=input("%s,do you want to choose rock,paper or scissors?"% user2)
# def compare(u1,u2):
#     if u1==u2:
#         return ("It's a tie!")
#     elif u1=='rock':
#         if u2=='scissors':
#             return ("Rock wins!")
#         else:
#             return ("paper wins!")
#     elif u1=='scissors':
#         if u2=='paper':
#             return ('scissor wins!')
#         else:
#             return ("rock wins!")
#     elif u1=='paper':
#         if u2=='rock':
#             return ("paper wins!")
#         else:
#             return ("scissors win!")
#     else:
#         return ("invalid input you have not entered rock,paper or scissors try again.")
#         sys.exit()
#
# print((compare(user1_answer,user2_answer)))




# ETL Project Assignment

# import pandas as pd
# df_xl=pd.read_excel("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/ExcelETL.xlsx")
# print(df_xl)
#
# df_json=pd.read_json("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/sample3.json")
# print(df_json)
#
# df_csv=pd.read_csv("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/CSVETL.csv")
# print(df_csv)
#
# df_all=pd.concat([df_xl,df_json,df_csv],axis=0)
# print(df_all)
# df_all.sort_values(by='ID',inplace=True)
# print(df_all)
#
# import psycopg2
# conn1=psycopg2.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Opened database successfully')
# # cur=conn.cursor()
# # cur.execute('CREATE TABLE TEST(ID INT NOT NULL,NAME TEXT NOT NULL)')
# # print('Table created successfully')
# # conn.commit()
# # conn.close()
# # cur.execute()
# conn1.autocommit = True
# cursor = conn1.cursor()
#
# # drop table if it already exists
# cursor.execute('drop table if exists test')
#
# sql = '''CREATE TABLE test(ID int,NAME char(20));'''
#
# cursor.execute(sql)
#
# # import the csv file to create a dataframe
# data = pd.read_csv("C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/CSVETL.csv")
#
# data = data[["ID", "NAME"]]
# # Create DataFrame
# print(data)
#
# # converting data to sql
# data.to_sql('test', conn, if_exists='replace')
#
# # fetching all rows
# sql1 = '''select * from TEST;'''
# cursor.execute(sql1)
# for i in cursor.fetchall():
#     print(i)
#
# conn1.commit()
# conn1.close()

# ETL mail from trainer

# import pandas as pd
# import psycopg2 as pg
# filepath_csv="C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/student.csv"
# filepath_json="C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/student_data.json"
# filepath_xlsx="C:/Users/hrudramu/OneDrive - Cisco/Documents/MS SQL_Learn/student_data1.xlsx"
#
# df_csv=pd.read_csv(filepath_csv)
# print(df_csv)
# df_json=pd.read_json(filepath_json)
# print(df_json)
# df_xlsx=pd.read_excel(filepath_xlsx,sheet_name="Sheet1")
# print(df_xlsx)
#
# df_final=df_csv.append(df_xlsx).append(df_json)
# print(df_final)
# connection = pg.connect(database='postgres',user='postgres',password='admin',host='127.0.0.1',port='5432')
# print('Connection success')
# dataframe = psql.DataFrame("SELECT * FROM category", connection)
# df = pd.read_sql_query('select * from student',con=connection)
# print(df)
# cur=conn.cursor()
# readt=cur.execute("select * from company3")
# print(readt)
# df_final.to_sql('student1', con=connection, if_exists='replace',
#             index=False)
# from sqlalchemy import create_engine
# engine = create_engine('postgresql://postgres:admin@127.0.0.1:5432/postgres')
# df_final.to_sql('student1', engine)


#1. Day 27 Assignment to find pi value for nth term with input

# import math
# pie=int(input("How many Decimal ?"))
# while pie>50:
#     print("Number to Large")
#     pie=int(raw_input("How many Decimal"))
# else:
#     print('%.*f'%(pie,math.pi))

# 2.Day 27 Create a Python project to get the value of e to n number of decimal places.
# Note: Input a number and the program will generate e to the 'nth digit





# Decode A Web Page Two Solutions
import requests
from bs4 import BeautifulSoup4

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

for elem in all_p_cn_text_body[7:]:
  print(elem.text)










