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