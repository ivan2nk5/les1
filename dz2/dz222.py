import random

class Student:

    def __init__(self, name):
        self.name = name
        self.glad = 50
        self.progress = 0.5
        self.alive = True
        self.money = 555

    def study(self):
        print("time to study")
        self.progress += 0.05
        self.glad -= 2

    def sleep(self):
        print("time to sleep")
        self.glad += 3

    def chill(self):
        print("time to relax")
        self.glad += 4
        self.progress -= 0.01

    def earn_and_spend(self):
        self.money += 100
        # Тратит случайную сумму от 30 до 60
        spending = random.randint(30, 120)
        self.money -= spending
        print(f"Spent {spending} money")


        if spending > 50:
            self.glad += 10


        if self.money < 0:
            self.money = 0

    def additional_expenses(self, day):

        if day % 30 == 0:
            self.money -= 500
            print(f"Spent 500 money on education")

        if self.glad < 20:
            self.money -= 200
            self.glad += 20
            print(f"Spent 200 money on vacation to increase gladness")


        if self.money < 0:
            self.money = 0

    def is_alive(self):
        if self.progress < 0.2:
            print("too lazy")
            self.alive = False
        elif self.glad <= 0:
            print("depressed")
            self.alive = False
        elif self.money <= 0:
            print("bankrupt")
            self.alive = False


        if self.progress > 5:
            print("genius (progress > 5)")

        if not self.alive:
            print("is not alive due to condition:")
            if self.progress < 0.2:
                print("too lazy (progress < 0.2)")
            elif self.glad <= 0:
                print("depressed (glad <= 0)")
            elif self.money <= 0:
                print("bankrupt (money <= 0)")

    def end_day(self):
        print(
            f'gladness - {self.glad}\n'
            f'progress - {round(self.progress, 2)}\n'
            f'money - {self.money}\n'
        )

    def live(self, day):
        print(f"Day {day} of {self.name}'s life")
        self.earn_and_spend()
        self.additional_expenses(day)
        magic = random.randint(1, 3)
        if magic == 1:
            self.study()
        elif magic == 2:
            self.sleep()
        elif magic == 3:
            self.chill()
        self.end_day()
        self.is_alive()


bob = Student("bob")

for day in range(365):
    if not bob.alive:
        break
    bob.live(day)

if not bob.alive:
    print("bob is not alive")
else:
    print("bob survived the year")
