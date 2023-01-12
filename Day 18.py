# Multithreading in Python

# Importing the threading module
# import threading
# def print_cube(num):
#     # Function to print the cube of given number
#     print("cube:{}".format(num*num*num))
# def print_square(num):
#     print("square:{}".format(num*num))
#
# if __name__=="__main__":
#     # Creating thread
#     t1=threading.Thread(target=print_square,args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#     # Starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
#     # wait untill thread 1 is completely executed
#     t1.join()
#     t2.join()
#     print("Done!")

# Program to illustarte the concept of threading

# import threading
# import os
# def task1():
#     print("Task 1 assigned to thread :{}".format(threading.current_thread().name))
#     print("ID of process running task 1:{}".format(os.getpid()))
#
# def task2():
#     print("Task 2 assigned to thread:{}".format(threading.current_thread().name))
#     print("ID of process running task 2:{}".format(os.getpid()))
# if __name__=="__main__":
#     print("ID of process running main program:{}".format(os.getpid()))
#     print("Main thread name:{}".format(threading.current_thread().name))
#     t1=threading.Thread(target=task1,name="t1")
#     t2=threading.Thread(target=task2,name="t2")
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()