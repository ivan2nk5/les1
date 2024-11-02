import random


def __init__(self,
             name="Human",job=None  , home=None,car=None
    ):

    self.name = name
    self.job = job
    self.home  = home
    self.car = car

    self.money = 100
    self.gladness = 50
    self.food  = 50

    def_home(self):
        self.home = house()
    def get_car(self):
        self.car = auto(brands_car)

    def job(self):
        if self.car.drive():
            pass
        else:


    def eat(self):
        if self.home.food_amount <= 0:
            self.shopping("food")
        else:
            if self.food >= 100:
                self.food  = 100

            self.food += 5
            self.home.food_amount  -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if  self.car.fuel  < 20:
                self.shop("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += set.job.salary
            self.gladness -= self.job.gladness_less
            self.food -= 4

    def shop(self,  actiom):
        if self.car.drive():
            pass
         else:
            if self.car.fuel < 20:
             action = "fuel"
            else:
                 self.to_repair()
                return
        if actiom = "fuel":
            print("i bought  a fuel")
            self.money -= 100
            self.car.fuel += 80
        elif  actiom == "food":
            print("l  b s f")
            self.money -= 50
            self.homey -=  50
            self.home.food_amount +=  50

def chill(self):
        self.gladness += 10
        self.home.me += 5

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def iss_alive(self):
        pass

    def days_indexes(self):
        pass

    def  live(self):
        pass


brands_car =  {}

class  auto:
    def __int__(self  , brandss_list):
        self.brand =  random.choice(list(brandss_list))
        self.fuel =  brandss_list[self.brand]["fuel"]
        self.streg = brandss_list[self.brand]["streng"]
        self.consumption = brandss_list[self.brand]["com"

    def drive(self):
        if self.streg > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.streg -= 1
            return True
        else:
            print("car  no")
class house:
    def __init__(self):
        self.mess = 0
        self.food_amount = 0

job_list = {}
class  job:

    def __init__(self,job_list):

        self.job  = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

