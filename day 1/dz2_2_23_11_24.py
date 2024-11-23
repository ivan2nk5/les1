import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.is_alive = True

    def eat(self):
        if self.hunger < 100:
            food = random.randint(10, 30)
            self.hunger += food
            self.energy += 10
            print(f"{self.name} is eating and gained {food} hunger, energy is now {self.energy}.")
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        self.energy += 20
        print(f"{self.name} is sleeping and gained 20 energy.")

    def play(self):
        if self.energy > 10:
            self.happiness += 15
            self.energy -= 10
            print(f"{self.name} is playing, happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is too tired to play!")

    def check_status(self):

        if self.hunger <= 0:
            self.is_alive = False
            print(f"{self.name} has died from starvation.")
        elif self.energy <= 0:
            self.is_alive = False
            print(f"{self.name} has died from exhaustion.")
        elif self.happiness <= 0:
            self.is_alive = False
            print(f"{self.name} has died from depression.")
        else:
            print(f"{self.name}'s status: Hunger={self.hunger}, Energy={self.energy}, Happiness={self.happiness}")

    def live(self):
        action = random.choice([self.eat, self.sleep, self.play])
        action()
        self.check_status()


class Owner:#хозяин
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.money = 200
        self.is_bankrupt = False

    def feed_cat(self, cat):

        if self.money >= 50:
            self.money -= 50
            cat.eat()
            print(f"{self.name} fed {cat.name}. Money left: {self.money}")
        else:
            print(f"{self.name} doesn't have enough money to feed {cat.name}.")
            self.is_bankrupt = True

    def play_with_cat(self, cat):

        if self.energy >= 10:
            self.energy -= 10
            cat.play()
            print(f"{self.name} played with {cat.name}. Owner's energy: {self.energy}")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):

        self.energy += 20
        print(f"{self.name} is resting and gained 20 energy.")

    def check_status(self):

        if self.energy <= 0:
            print(f"{self.name} is too tired to take care of {cat.name}.")
        elif self.money <= 0:
            self.is_bankrupt = True
            print(f"{self.name} has gone bankrupt.")
        else:
            print(f"{self.name}'s energy: {self.energy}, Money: {self.money}")

cat = Cat("bobik")
owner = Owner("bob")


for day in range(10):
    print(f"\nDay {day + 1}:")

    if not cat.is_alive:
        print(f"{cat.name} has passed away.")
        break

    if owner.is_bankrupt:
        print(f"{owner.name} has gone bankrupt. The game is over.")
        break

    if owner.energy > 0:
        action = random.choice([owner.feed_cat, owner.play_with_cat, owner.rest])
        if action == owner.rest:
            action()
        else:
            action(cat)
    else:
        print(f"{owner.name} is too tired to take care of {cat.name}.")

    cat.live()
    owner.check_status()
    cat.check_status()

