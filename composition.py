#Composition pgm
class Os:
    def __init__(self):
        self.status = "Active"
        print("Os is installing")
    def getOs(self):
        print("Os is installed")
class Mobile:
    def __init__(self):
        self.Mname="Iqoo"
        self.O=Os()
        print("Mobile is ready")
M=Mobile()
print(M.Mname)
print(M.O.status)
M.O.getOs()
del M
M.O.getOs()

#Aggregation pgm
class Charger:
    def __init__(self):
        self.Cname='Asus Charger'
        print('Charger is ready')
    def getCharger(self):
        print('Charger is not working')
class Laptop:
    def __init__(self):
        self.Lname='Asus'
        self.R=''
        print('Laptop is ready')
    def getLaptop(self, A):
        self.R=A
L=Laptop()
C=Charger()
print(L.Lname)
L.getLaptop(C)
L.R.getCharger()
del L
C.getCharger()