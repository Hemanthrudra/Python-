# Python file  --Open ,Read or write,Close
import os

# 1.write operation
# f=open("data.txt",'w')
# f.write("This is first line\n")
# f.write("This is second line\n")
# f.close()

# 2.Read operation
# f=open("data.txt",'r')
# print(f.read())
# f.close()

# 3.read operation using for loop
# f=open("data.txt",'r')
# for line in f:
#     print(line,end='')

# 4.Append data into a file
# with open("data.txt",'a') as f:
#     f.write("This is third line")

# 5.Read operation
# with open('data.txt',encoding='cp1252',mode='r') as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.tell())
#     print(f.seek(0))
#     print(f.read())

# 6.Readline method

# with open("data.txt",encoding='cp1252',mode='r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.tell())
#     print(f.seek(0))
#     print(f.readlines())

# 7.Exclusive creation

# with open("data.txt",mode='x',encoding='cp1252') as f:
#     f.write("This is fourth line")

# Python Directory
# 1. To get current working directory
# import os
# print(os.getcwd())

# To change the directory
# import os
# print(os.getcwd())
# print(os.chdir("c:/"))
# print(os.getcwd())

# 3.To list of files and folder
# import os
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir('c:/'))

# 4.To create new directory
# print(os.listdir())
# print(os.mkdir('Test'))
# print(os.listdir())

# 5.To Rename directory
# print(os.listdir())
# print(os.rename('Test','Test1'))

# 6. To remove files
# print(os.listdir())
# os.remove('data.txt')
# print(os.listdir())

# 7.To remove empty directory
# print(os.listdir())
# os.rmdir('Test1')
# print(os.listdir())

# 8.To remove non empty directory
# import shutil
# print(os.listdir())
# shutil.rmtree('Test 2')
# print(os.listdir())
