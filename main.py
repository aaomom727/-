import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        brand = random.choice(list(brands_of_car.keys()))
        self.car = Auto(brand)

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(random.choice(list(job_list.keys())))
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car and self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if self.car and self.car.drive():
            if manage == "fuel":
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("Bought food")
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                print("Hooray! Delicious!")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15
        else:
            self.to_repair()

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"Today is the {day}th day of {self.name}'s life.")
        print(f"Money: {self.money}, Satiety: {self.satiety}, Gladness: {self.gladness}")
        print(f"Food: {self.home.food}, Mess: {self.home.mess}")
        print(f"{self.car.brand} -> Fuel: {self.car.fuel}, Strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
            print("Settled in the house.")
        if self.car is None:
            self.get_car()
            print(f"I bought a car: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I got a job: {self.job.title} with a salary of {self.job.salary}.")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat.")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but the house is messy. Cleaning instead.")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Time to work!")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car.")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Time to work!")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping("delicacies")

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = brands_of_car[brand]["fuel"]
        self.strength = brands_of_car[brand]["strength"]
        self.consumption = brands_of_car[brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            return True
        else:
            self.strength -= 1
            print("The car cannot move.")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class RepairShop:
    def __init__(self, name="Auto Repair"):
        self.name = name
        self.repair_cost = 50

    def repair_car(self, car):
        if car.strength < 100:
            print(f"Repairing {car.brand} car...")
            car.strength = 100
            return True
        else:
            print(f"{car.brand} car is already in good condition!")
            return False




class Job:
    def __init__(self, title, salary, gladness_less):
        self.title = title
        self.salary = salary
        self.gladness_less = gladness_less

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break




