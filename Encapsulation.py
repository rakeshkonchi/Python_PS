#pgm using private var
class Book:
    def __init__(self,p):
        self.__page=p # private var
B=Book(25)
print(B.__page)

class Book:
    def __init__(self,p):
        self.__page=p
    def setter(self,N):
        if N>0:
            self.__page=N
        else:
            pass
    def getter(self):
        return self.__page
B=Book(100)
res=B.getter()
print(res)
B.setter(200)
res1=B.getter()
print(res1)
B.setter(-300)
res2=B.getter()
print(res2)