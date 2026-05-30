# class Insta:
#     def __init__(self):
#         self.a=100
#         self.b=200
# class Snap(Insta):
#     def __init__(self):
#         Insta.__init__(self)
#         self.c=300
# S=Snap()
# print(S.c)
# print(S.a)
# print(S.b)

#Normal approach
# class House:
#     def __init__(self):
#         self.A=420
#         print(self.A)
#         print(self)
# class Hall(House):
#     def __init__(self):
#         self.A=520
#         print(self.A)
#         print(self)
#
#         House.__init__(self)
# class Room(Hall):
#     def __init__(self):
#         self.A=620
#         print(self.A)
#         print(self)
#
#         Hall.__init__(self)
# R=Room()
# print(R.A)

#standard approach
# class Parent:
#     def __init__(self):
#         self.a=50
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
# C=Child()
# print(C.a)

#inheriting parent method
# class Parent:
#     def strict(self):
#         print("Parent is very strict")
# class Child(Parent):
#     def Lazy(self):
#         print("Child is lazy ")
# C=Child()
# C.Lazy()
# C.strict()

# class A:
#     def sleep(self):
#         print("Akash")
# class B(A):
#     def sleep(self):
#         print("Akshaya")
# res=B()
# res.sleep()
# res.sleep()

# class A:
#     def sleep(self):
#         print("Akash")
# class B(A):
#     def sleep(self):
#         print("Akshaya")
#         super().sleep()
# res=B()
# res.sleep()

# class A:
#     def calci(self,A):
#         print(A)
# class B(A):
#     def calci(self,A,B):
#         print(A,B)
# class C(B):
#     def calci(self,A,B,C):
#         print(A,B,C)
# res=C()
# res.calci(10,20,30)
# res.calci(10,20)
# res.calci(10)

# class A:
#     def run(self):
#         print(1)
# class B(A):
#     def run(self):
#         print(2)
#         super().run()
# class C(A):
#     def run(self):
#         print(3)
#         super().run()
# class D(B,C):
#     def run(self):
#         print(4)
#         super().run()
# res=D()
# res.run()
# print(D.mro())

# class A:
#     def run(self):
#         print('A')
# class B(A):
#     def run(self):
#         print('B')
#         super().run()
# class C(A):
#     def run(self):
#         print('C')
#         super().run()
# class D(A):
#     def run(self):
#         print('D')
#         super().run()
# class E(B,C):
#     def run(self):
#         print('E')
#         super().run()
# class F(C,D):
#     def run(self):
#         print('F')
#         super().run()
# class G(E,F):
#     def run(self):
#         print('G')
#         super().run()
# res=G()
# res.run()
# print(G.mro())

# class A:
#     def run(self):
#         print('A')
# class B:
#     def walk(self):
#         print('B')
# class C(B,A):
#     def run(self):
#         print('C')
#         super().run()
# res=C()
# res.run()
# res.walk()

class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def run(self):
        print("Animal is running")
    def name(self):
        pass
class Lion(Animal):
    def name(self):
        print("Animal name is Lion")
class Tiger(Animal):
    def name(self):
        print("Animal name is Tiger")
class Cat(Animal):
    def name(self):
        print("Animal name is Cat")
L=Lion()
T=Tiger()
C=Cat()
def zoo(ref):
    ref.eat()
    ref.sleep()
    ref.run()
    ref.name()
zoo(L)
zoo(T)
zoo(C)