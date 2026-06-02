class student:
    def __init__(self):
        self.name = "Rakesh"
        self.age = 22
        self.usn = 420
    def study(self):
        print("Rakesh is not studying")
s1 = student()
print(s1.name)
print(s1.age)
print(s1.usn)
s1.study()


A = 11
B = 22
C = 11
D = 33
E = 22
print(id(A))
print(id(B))
print(id(C))
print(id(D))
print(id(E))
print(A is B)
print(A is C)
print(B is E)

print("enter a number:")
A=(input())
print("enter another number:")
B=(input())
C=A+B
print(C)

print("enter a number:")
A=int(input())
print("enter another number:")
B=int(input())
C=A+B
print(C)

A=int(input("enter a number:"))
B=int(input("enter another number:"))
C=A+B
print(C)

print("Enter  a number:")
A=int(input())
print("Enter another number:")
B=int(input())
if A>B:
    print("A is bigger")
elif B>A:
    print("B is bigger")
else:
    print("A and B are equal")

a=int(input("enter a number:"))
if a>0:
    print("number is positive")
elif a<0:
    print("number is negative")
else:
    print("number is zero")

marks=int(input("enter the marks:"))
if 100>=marks>=90:
    print("A grade")
elif 65<=marks<90:
    print("B grade")
elif 45<=marks<65:
    print("C grade")
elif 35<=marks<45:
    print("D grade")
elif marks<35:
    print("Fail")
else:
    print("invalid input")

class student:
    def __init__(self):
        self.name = "Rakesh"
        self.age = 22
        self.usn = 420
    def study(self):
        print("Rakesh is not studying")
s1 = student()
print(s1.name)
print(s1.age)
print(s1.usn)
s1.study()
