class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer,Swimmer):
    pass

#objects

d = Duck()
d.fly()
d.swim()

