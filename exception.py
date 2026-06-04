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