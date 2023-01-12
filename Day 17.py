# Python Logical errors (Exceptions)

# print(dir(locals()['__builtins__']))

# Importing module systems
# import sys
# randomList=['a',0,2]
# for entry in randomList:
#     try:
#         print("The entry is",entry)
#         r=1/int(entry)
#         break
#     except:
#         print("Oops!",sys.exc_info()[0],"occured.")
#         print("Next entry.")
#         print()
# print("The reciprocal of",entry,"is",r)

import sys
# randomList=['a',0,2]
# for entry in randomList:
#     try:
#         print("The entry is",entry)
#         r=1/int(entry)
#         break
#     except Exception as e:
#         print("Oops!",e.__class__,"occured.")
#         print("Next entry.")
#         print()
# print("The reciprocal of",entry,"is",r)

# # Catching specific Exceptions in Python
# try:
#     # Do something
#     pass
# except ValueError:
#     # Handle ValueError exception
#     pass
# except (TypeError,ZeroDivisionError):
#     # handle multiple exception
#     # TypeError and ZeroDivisionError
#     pass
# except:
#     # handle all other exceptions
#     pass

# Raising Exception in Python
# raise KeyboardInterrupt
# raise MemoryError("This is an argument")
# try:
#     a=int(input("Enter a positive integer:"))
#     if a<=0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)

# # Python try with else clause
# try:
#     num=int(input("Enter a number:"))
#     assert num%2==0
# except:
#     print("Not an even number!")
# else:
#     reciprocal=1/num
#     print(reciprocal)
#
# try:
#     f=open("test.txt",encoding='utf-8')
# finally:
#     f.close()