
# Inheritance.

# 1. Single level inheritance
# class A:
#     pass
# class B(A):
#     pass
#
# class student:
#     def printdetails(self):
#         print("I am raj")
# class main(student):
#     pass
# obj=main()
# obj.printdetails()

# 2.Multiple inheritance

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass

# class student:
#     def printdetails(self):
#         print("I am Raj")
# class address:
#     def printaddress(self):
#         print("I am from Bangalore")
# class main(student,address):
#     pass
# obj=main()
# obj.printaddress()
# obj.printdetails()

# 3.Multilevel Inheritance

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass

# class student:
#     def printdetails(self):
#         print("I am Raj")
# class address(student):
#     def printaddress(self):
#         print("I am from Bangalore")
# class main(address):
#     pass
# obj=main()
# obj.printdetails()
# obj.printaddress()

# Properties inheritance (Using Class instructor )

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printdetails(self):
#         print(self.name,self.age)
# class address(student):
#     def __init__(self,name,age,add):
#         self.add=add
#         student.__init__(self,name,age)
#     def printfulldetails(self):
#         print(self.name,self.age,self.add)
# class main(address):
#     pass
# obj1=main("Raj",23,"HBR")
# obj2=main("sam",26,"HSR")
# obj1.printdetails()
# obj1.printfulldetails()
# obj2.printfulldetails()

