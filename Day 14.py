
# Decorator
# def first(msg):
#     print(msg)
# first("Hello")
# second=first
# second('Hello')
#
# def inc(x):
#     return x+1
# def dec(x):
#     return x-1
# def operate(func,x):
#     result=func(x)
#     return result
# print(inc(3))
# print(dec(3))

# def is_called():
#     def is_returned():
#         print('Hello')
#     return is_returned()
# new=is_called()

# def make_pretty(func):
#     def inner():
#         print('I got Decorated')
#         func()
#     return inner
# def ordinary():
#     print('I am ordinary')
# @make_pretty
# def ordinary():
#     print('I am ordinary')
# def ordinary():
#     print('I am ordinary')
#     ordinary=make_pretty(ordinary)


# def divide(a,b):
#     return a/b
# divide(2,5)
#python print (divide)

# def smart_divide(func):
#     def inner(a,b):
#         print('I am going to divide',a,'and',b)
#         if b==0:
#             print('whoops! cannot divide')
#             return
#         return func(a,b)
#     return inner
# @smart_divide
# def divide(a,b):
#     print(a/b)

# divide(2,5)
# divide(2,0)

# def works_for_all(func):
#     def inner(*args,**kwargs):
#         print('I can decorate any function')
#         return func(*args,**Kwargs)
#     return inner

# Chaining decorators in Python
# def star(func):
#     def inner(*args,**kwargs):
#         print('*'* 30)
#         func(*args,**kwargs)
#         print('*'* 30)
#     return inner
# def percent(func):
#     def inner(*args,**kwargs):
#         print('%'*30)
#         func(*args,**kwargs)
#         print('%'*30)
#     return inner
# @star
# @percent
# def printer(msg):
#     print(msg)
#
# printer('Hello')

# the above syntax of
# @star
# @percent
# def printer(msg):
#     print(msg)

# is equivalent to

# def printer(msg):
#     print(msg)
# printer=star(percent(printer))

# The order in which we chain decorators matter.
# if we had reversed the order as,
# @percent
# @star
# def printer(msg):
#     print(msg)

