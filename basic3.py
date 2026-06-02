class Car:
    def __init__(self):
        self.Brand = "TATA"
        self.color = "White"
        self.model = 2019
    def on(self):
        print("Car is started")
    def move(self):
        print("Car is moving")
    def off(self):
        print("Car is off")
c = Car()
print(c.Brand)
print(c.color)
print(c.model)
c.on()
c.move()
c.off()

