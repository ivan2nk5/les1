import random
import time

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.food = 50
        self.alive = True

    def def_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_car)

    def eat(self):
        if self.home.food_amount <= 0:
            self.shop("food")
        else:
            if self.food >= 100:
                self.food = 100
            self.food += 5
            self.home.food_amount -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shop("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.food -= 4

    def shop(self, action):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                action = "fuel"
            else:
                self.to_repair()
                return
        if action == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 80
        elif action == "food":
            print("I bought food")
            self.money -= 50
            self.home.food_amount += 50

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.home.mess = 0

    def to_repair(self):
        self.car.strength = 100

    def is_alive(self):
        if self.gladness <= 0 or self.food <= 0 or self.money <= 0:
            print(f"{self.name} is no longer alive.")
            self.alive = False
        return self.alive

    def days_indexes(self, day):
        day_info = f"Day {day} of {self.name}'s life"
        print(f"{day_info}\n{'-'*len(day_info)}")
        print(f"Money: {self.money}")
        print(f"Gladness: {self.gladness}")
        print(f"Food: {self.food}")

    def live(self, day):
        if not self.is_alive():
            return
        self.days_indexes(day)
        action = random.choice(["eat", "work", "chill", "clean_home"])
        if action == "eat":
            self.eat()
        elif action == "work":
            self.work()
        elif action == "chill":
            self.chill()
        elif action == "clean_home":
            self.clean_home()
        print(f"Action: {action}")

        # Шанс на смерть
        death_chance = random.randint(1, 100)
        if death_chance <= 5:  # 5% шанс на смерть
            print(f"{self.name} died unexpectedly.")
            self.alive = False

class Auto:
    def __init__(self, brands_list):
        self.brand = random.choice(list(brands_list))
        self.fuel = brands_list[self.brand]["fuel"]
        self.strength = brands_list[self.brand]["strength"]
        self.consumption = brands_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot drive")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food_amount = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

brands_car = {
    "Toyota": {"fuel": 100, "strength": 100, "consumption": 10},
    "BMW": {"fuel": 80, "strength": 120, "consumption": 15}
}

job_list = {
    "Developer": {"salary": 100, "gladness_less": 10},
    "Teacher": {"salary": 50, "gladness_less": 5}
}

def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def error_logging(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            raise e
    return wrapper

# Приклад використання декораторів
@time_function
@error_logging
def example_function():
    time.sleep(1)  # Симуляція роботи функції
    return "Function completed"

def test_time_function():
    result = example_function()
    assert result == "Function completed", "Test failed: Incorrect function result"
    print("Test passed: Function result is correct")

test_time_function()

# Симуляція життя
human = Human(name="John", job=Job(job_list), home=House(), car=Auto(brands_car))
for day in range(1, 8):
    human.live(day)
    if not human.alive:
        break
