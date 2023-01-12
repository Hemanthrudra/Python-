
# # # Function
# def greet(name,msg):
#     print("Hello",name,msg)
# greet("Raj", "GM")

# def CheckNumber(x):
#     if x==1:
#         return x
#     else:
#         return -x
#
#
#
# print(CheckNumber(90))

# def discount(PAmount):
#     if PAmount>1000:
#         return 500
#     else:
#         return 0
# def totalAmount(PAmount):
#     discAmount=discount(PAmount)
#     finalAmount=PAmount-discAmount
#     print(finalAmount)
# totalAmount(11000)

# Function Recursion
#
# def fact(x):
#     if x==1:
#         return x
#     else:
#         return fact(x-1)*x
# print(fact(4))

# Lambda function
# One method
# double=lambda x,y:x*y
# print(double(5,2))

# Second method
# def double(x,y):
#     return x*y
# d=double(5,2)
# print(d)

# Function Argument
# def greet(name,msg):
#     print("Hello",name,msg)
# greet("Raj","GM")
# greet(name="Raj",msg='GM')
# greet(msg='GM',name='Raj')
# greet()    -------This thorws errorTypeError:
# greet() missing 2 required positional arguments: 'name' and 'msg'

# Using default parameter
# def greet(name='Raj',msg='GM'):
#     print('Hello',name,msg)
# greet()
# greet('Raja')
# greet('Raja',msg='GE')
# greet(msg='GE')
# greet(name='hemanth')

# Non default argument follow default argument
#
# def greet(name,msg='GE'):
#     print('Hello',name,msg)
# greet('raj')
# greet('Costly')