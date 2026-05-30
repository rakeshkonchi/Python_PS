# L=[1,2,3,4,5]
# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# res=list(filter(even,L))
# print(res)

# L=[1,2,3,4]
# def square(num):
#     return num*num
# res=list(map(square,L))
# print(res)

# K=[3,4,5,6]
# def odd(num):
#     if num%2!=0:
#         return True
#     else:
#         return False
# def cube(num):
#     return num**3
# res=list(map(cube,filter(odd,K)))
# print(res)

# K=[3,4,5,6]
# res=list(map(lambda num:num**3,filter(lambda num1:num1%2!=0,K)))
# print(res)

# print(list(map(lambda num:num**3,filter(lambda num1:num1%2!=0,[3,4,5,6]))))

# def fun1():
#     yield 1
#     yield 2
#     yield 3
# X=fun1()
# print(id(fun1))
# print(id(X))
# print(type(fun1))
# print(type(X))
# print(next(X))
# print(next(X))
# print(next(X))
# print(next(X))