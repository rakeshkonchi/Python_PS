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