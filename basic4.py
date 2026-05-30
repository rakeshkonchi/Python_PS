class Actor:
    def __init__(self):
        self.name = "Rakshit Shetty"
        self.age = 40
        self.gfname = "Sundri"
    def act(self):
        print("Rakshit Shetty loves Sundri")
A = Actor()
print(A.gfname)
print(A.age)
A.gfname = "Rashmika"
print(A.gfname)
A.noOfMovies = 20
del A.age
print(A.age)