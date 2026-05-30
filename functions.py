#no p, no rv
# def add():
#     A=10
#     B=20
#     C=A+B
#     print(C)
# add()

#no p, with rv
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# res=add()
# print(res)

#with p, no rv
# def add(a,b):
#     c=a+b
#     print(c)
# x=10
# y=20
# add(x,y)

#with p, with rv
# def add(a,b):
#     c=a+b
#     return c
# x=10
# y=20
# res=add(x,y)
# print(res)

#Invoking fun through var
# def fun1():
#     print('MI')
# def fun2():
#     print('RCB')
# ptr1=fun1
# ptr2=fun2
# ptr1()
# ptr2()
# print(id(ptr1))
# print(id(fun1))

#Nested fun
# def outer():
#     print("Entering outer")
#     def inner():
#         print("Entering inner")
#     inner()
# outer()

# def outer():
#     print("Entering outer")
#     def inner():
#         print("Entering inner")
# outer()
# inner()

# A=100
# def outer():
#     A=200
#     B=300
#     print(A)
#     print(B)
#     def inner():
#         A=400
#         B=500
#         print(A)
#         print(B)
#     print(A)
#     inner()
# print(A)
# outer()

# A=10
# def fun1():
#     A=11
#     B=22
#     print(A)
#     print(B)
# def fun2():
#     A=12
#     B=33
#     print(A)
# print(A)
# fun1()
# print(A)
# fun2()
# print(A)

# A=50
# def outer():
#     global A
#     A=25
#     print(A)
# outer()
# print(A)

# #A=20
# def outer():
#     #A=30
#     def inner():
#         #A=40
#         print(A)
#     inner()
# outer()

# from math import pi
# # pi=20
# def outer():
#     #pi=30
#     def inner():
#         #pi=40
#         print(pi)
#     inner()
# outer()

#decorator function
# def deco():
#     print('How are you')
# def outer(par):
#     print('Hi baby')
#     def inner():
#         print('good afternoon')
#         res=par
#         res()
#     return inner
# res1=outer(deco)
# res1()

# def deco():
#     msg='pentagon'
#     return msg
# def outer(par):
#     def inner():
#         res=par()
#         res1=res.upper()
#         print(res1)
#     return inner
# res2=outer(deco)
# res2()

# A=100
# def outer():
#     B=200
#     C=300
#     print(B)
#     print(C)
#     def inner():
#         D=400
#         print(D)
#     inner()
# outer()
# print(A)
# class Employee:
#     E=500
#     def __init__(self):
#         self.F='Rohit'
#     def work(self):
#         print('MI')
#         G=600
#         print(G)
# Res=Employee()
# Res.work()
# print(Employee.E)
# print(Res.F)
# outer()

# Case 1 Higher order(decorator fun)
# def fun1():
#     A=10
#     B=20
#     C=A+B
#     print(C)
# def fun2(arg):
#     print('Hello')
#     arg()
# res=fun1
# fun2(res)

#case 2 HO(closure)
# def outer():
#     print('rose')
#     def inner():
#         print('jack')
#     return inner
# res=outer()
# res()

# def square(num):
#     return num * num
# res=square(5)
# print(res)

# square=lambda num: num*num
# res=square(5)
# print(res)

# def sub(A, B):
#     return A - B
# res=sub(100,40)
# print(res)

sub=lambda a,b: a-b
res=sub(100,40)
print(res)