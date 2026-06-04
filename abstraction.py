from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class Gpay(Payment):
    def pay(self, amount):
        if amount > 0:
            print(amount, "received through Gpay")
        else:
            print("Amount cannot be negative/zero")
class Paytm(Payment):
    def pay(self, amount):
        if amount > 0:
            print(amount, "received through Paytm")
        else:
            print("Amount cannot be negative/zero")

G=Gpay()
P=Paytm()
G.pay(100)
P.pay(1000)
G.pay(-200)