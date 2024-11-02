import random

class human:
    def __init__(self, name="human"):
        self.name = name

class auto:

    def __init__(self,brand):
        self.brand = brand
        self.passengers  = []
    def add_passenger(self,*args):
        for p in args:
            self.passengers.append(p)

    def  print_p_name(self):
        if self.passengers:
            print(f"n of {self.brand} passengers")
        for passenger  in self.passengers:
            print(passenger.name)
        else:
            print("t  a n o passengers")

a = input("1")
a = human(name=a)
kate = human(name="kate")
nick = human(name="nick")

car = auto("mers")
car.add_passenger(a , kate , nick)

car.print_p_name()