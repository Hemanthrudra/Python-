# Iterators
# Iterating through an Iterator

# Define a list
# my_list=[4,7,0,3]

# get an iterator using iter()
# my_iter=iter(my_list)

# Iterate through it using next ()
# output 4
# print(next(my_iter))

# output 7
# print(next(my_iter))

# Output 0
# print(next(my_iter))

# Output 3
# print(next(my_iter))

# This This will raise error , no items left

# next(my_iter)

# Iterator using for Loop
my_iterable = [4, 7, 0, 3]
# for element in my_list:
#     print(element)

# for element in my_iterable:
#     # Do something with element
#
# # Create an iterator object from that iterable
# iter_obj=iter(iterable)
# # Infinite loop
#
# while True:
#     try:
#         element=next(iter_obj)
#
#     except StopIteration:
#         break

# class PowTwo:
#     # Class to implement an iterator of powers of two
#     def __init__(self,max=0):
#         self.max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         if self.n<=self.max:
#             result=2 ** self.n
#             self.n +=1
#             return result
#         else:
#             raise StopIteration

# Create an object
# numbers=PowTwo(3)
# i=iter(numbers)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# with for loop
# for i in PowTwo(5):
#     print(i)

# Python infinite iterators
# int()
# inf=iter(int,1)
# next(inf)
# next(inf)

# Infinite iterator to return all odd numbers

# class InfIter:
#     def __iter__ (self):
#         self.num= 1
#         return self
#
#     def __next__ (self):
#          num = self.num
#          self.num += 2
#          return num
# a=iter(InfIter())
# next(a)
# next(a)

# 2.Generators in Python
# A simple generator function
# def my_gen():
#     n=1
#     print('This is printed first')
# #     Generator function contains yield statements
#     yield n
#     n+=1
#     print('This is printed second')
#     yield n
#     n+=1
#     print('This is printed at last')
#     yield n
# a=my_gen()
# next(a)
# next(a)
# next(a)
# next(a)

# Using for loop

# def my_gen():
#     n = 1
#     print('This is printed first')
#     yield n
#     n+= 1
#     print('This is printed second')
#     yield  n
#     n+=1
#     print('This is printed at last')
#     yield n
# for item in my_gen():
#     print(item)

# Example of generator that reverses a string
# def rev_str(my_str):
#     length =len(my_str)
#     for i in range(length -1,-1,-1):
#         yield my_str[i]
# for char in rev_str("Hello"):
#     print(char)

# Initialize the list
# my_list=[1,3,6,10]

# Square each term using list comprehension
# list_=[x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
# generator=(x**2 for x in my_list)
# print(list_)
# print(generator)

# my_list=[1,3,6,10]
# a=(x**2 for x in my_list)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# next(a)
# sum(x**2 for x in my_list)
# max( x**2 for x in my_list )

# 1.Easy to implement

# class PowTwo:
#     def __init__(self,max=0):
#         self.n=0
#         self.max=max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.max:
#             raise StopIteration
#         result=2**self.n
#         self.n+=1
#         return result

# Using for loop
# def PowTwogen(max=0):
#     n=0
#     while n<max:
#         yield 2 ** n
#         n+=1

# def all_even():
#     n=0
#     while True:
#         yield n
#         n += 2

# Fibonacci Numbers

# def fibonacci_numbers(nums):
#     x,y = 0,1
#     for i in range(nums):
#         x, y=y,x+y
#         yield x
# def square(nums):
#     for num in nums:
#         yield num**2
# print(sum(square(fibonacci_numbers(10))))
