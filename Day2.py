# Number
# 1.Integer
a=5
# print(a)
# print(type(a))
# print(isinstance(a,int))
# 2.Flaot
a=10.5
# print(a)
# print(type(a))
# print(isinstance(a,float))
# 3.complex
a=1+2j

# print(a)
# print(type(a))
# print(isinstance(a,complex))

# String
name="Rajkumar"
# print(name)
# print(name[0])
# print(name[0:3])
# name[0]='K'
# print(name)

# List
l=[4,5.5,"Rajkumar"]
# print(l)
# print(l[0])
# print(l[0:2])
# print(l[2][0:3])
l[0]=50
# print(l)

# Tuple
t=(4,5.5,"Rajkuamr")
# print(t)
# print(t[0])
# print(t[0:2])
# t[0]=50
# print(t)

# Set
s={1,2,1,2,3,3}
# print(s)
s1={1,2,3,4}
s2={3,4,5,6}
s3=s1.intersection(s2)
# print(s3)
s4=s1.union(s2)
# print(s4)

# Dictionary
d={'id':1,'name':"Raj"}
# print(d)
# print(d['id'])
# print(d['name'])

# Day 3 - Type Conversion

# 1.int to float
a=10
b=10.5
# print(type(a))
# print(type(b))
sum=a+b
# print(sum)
# print(type(sum))

# 2.float to complex
a=10.5
b=1+2j
# print(type(a))
# print(type(b))
sum=a+b
# print(sum)
# print(type(sum))

# 3.String to int (without explicit)
a='400'
b=10
# print(type(a))
# print(type(b))
# sum =a+b
# print(sum)      (This throws error as we cant add int and string)
# print(sum)
# print(type(sum))

# 4. String to int with explicit
a='400'
b=10
# print(type(a))
# print(type(b))
# a=int(a)                (Here we convert string to int)
# print(type(a))
# sum =a+b
# print(sum)
# print(type(sum))

# [] for  List
# () for tuple
# {} for set
# {:} for dictionary

# 5.list to tuple
l=[4,5.5,6]
# print(l)
# print(type(l))
# t=tuple(l)
# print(t)
# print(type(t))

# 6.Tuple to list
t=(4,5,6)
# print(t)
# print(type(t))
l=list(t)
# print(l)
# print(type(l))


# 7.Tuple to set

a=(4,5,6,6,7,5)
# print(a)
# print(type(a))
s=set(a)
# print(s)
# print(type(s))

# 8.Set to dictionary
s={1,2,3,4}
# print(s)
# print(type(s))
# In from keys ( 's' is Value , and ',1' is a common value considered for execution you can give any number
d=dict.fromkeys(s,2)
# print(d)
# print(type(d))

