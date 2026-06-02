class User:
    def __init__(self,sid, sname):
        self.id = sid
        self.name = sname
U1 = User(1,"kohli")
U2 = User(2,"rahul")
print(U1.id)
print(U2.id)

brand = "Iqoo"
class Phone:
    color = "Black"
    def __init__(self, r, p):
        self.ram = r
        self.processor = p
    def charge(self):
        print(Phone.color)
        print(brand)
p1 = Phone(8,"Snapdragon")
print(p1.processor)
p1.charge()
print(Phone.color)