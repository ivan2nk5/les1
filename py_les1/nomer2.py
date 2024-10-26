import random

class Student:

    def __init__(self, name):
        self.name = name
        self.glad = 50
        self.progres = 0
        self.alive= True


    def study(self):
        print("time to study")
        self.progres += 0.12
        self.glad  -= 3

    def sleep(self):
        print("time to sleep")
        self.glad += 3

    def chill(self):
        print("time of relax")
        self.glad += 5
        self.progres -= 0.05

    def is_alive(self):
        if self.progres < 0.5:
            print("too lazy")
            self.alive = False
        elif self.glad  <= 0:
            print("dep")
            self.alive = False
        elif self.progres > 5:
            print("genius")
            self.alive = False

    def end_day(self):
        print(
            f'gladness - {self.glad}\n'
            f"progress - {round(self.progres,2)}"
            f""
        )
    def live (self,day):
        print(
            f"Day {day}of {self.name} life"
        )
        magic = random.randint(1,3)
        if magic == 1:
            self.study()
        elif magic  == 2:
            self.sleep()
        elif magic == 3:
            self.chill()
        self.end_day()
        self.is_alive()


bob = Student("bob")
for day in range(365):
    if  bob.is_alive ==  False:
        break
    bob.live(day)