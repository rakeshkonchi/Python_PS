class Fan:
    def __init__(self):
        self.brand = "usha"
        self.color = "white"
        self.cost = 3000
        self.blades = 3

    def on(self):
        print("Fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("Fan is off")

f1 = Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.blades)
f1.on()
f1.rotate()
f1.off()
