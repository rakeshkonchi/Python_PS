A=int(input("Enter a number: "))
B=int(input("Enter another number: "))
C=A/B
print(C)

A=int(input("Enter a number: "))
B=int(input("Enter another number: "))
try:
    C=A/B
    print(C)

except Exception as e:
    print("Hello")
    print(e)

def fun1():
    print("Entering fun1")
    res=10/0
    print(res)
    print("leaving fun1")
def fun2():
    print("Entering fun2")
    try:
        fun1()
    except Exception as e:
        print("Error")
    print("leaving fun2")
print("Program started")
fun2()
print("Program ended")

A=int(input("Enter a number"))
B=int(input("Enter another number"))
try:
    C=A/B
    print(C)
except Exception as e:
    print("Error")
else:
    print("No error")

A=int(input("Enter a number"))
B=int(input("Enter another number"))
try:
    C=A/B
    print(C)
except Exception as e:
    print("Error")
else:
    print("Error")
finally:
    print("Program execution completed")