# 27-10-2022
# Polymorphism , Means =Many forms

# 1.Using Built in functon
# print(len("Hemanth"))
# print(len([1,2,3]))

# 2.Using User defined function
# def add(x,y,z=0):
#     print(x+y+z)
# add(5,2)
# add(5,2,5)

# 3.Using Class example
# 3.1
# class India:
#     def type(self):
#         print("India is a developing Country")
#     def language(self):
#         print("Hindi is most widely speaking language in India")
# class USA:
#     def type(self):
#         print("USA is a developed Country")
#     def language(self):
#         print("English is most widely speaking language in USA")
# obj_India=India()
# obj_USA=USA()
# for val in (obj_India,obj_USA):
#     val.type()
#     val.language()

# 3.2

# class Bird:
#     def intro(self):
#         print("There are many types of bird")
#     def flight(self):
#         print("Some Birds can fly but some can't")
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrow can fly")
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostrich Can't fly")
# obj_Bird=Bird()
# obj_Sparrow=Sparrow()
# obj_Ostrich=Ostrich()
# for val in (obj_Bird,obj_Sparrow,obj_Ostrich):
#     val.intro()
#     val.flight()

