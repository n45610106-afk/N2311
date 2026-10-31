import random

class House:
    def __init__(self):
        self.food = 30
        self.mess = 0


class Job:
    def __init__(self):
        self.name = "Python Developer"
        self.salary = 50


# Новий клас
class Pet:
    def __init__(self):
        self.name = "Bobby"
        self.happiness = 50

    def play(self):
        self.happiness += 10
        print(f"Улюбленець {self.name} грається! Настрій: {self.happiness}")


class Human:
    def __init__(self, name="Bob"):
        self.name = name
        self.money = 100
        self.satiety = 50
        self.house = House()
        self.job = Job()
        self.pet = Pet()

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 20
            self.house.food -= 10
            print(f"{self.name} пообідав. Ситість: {self.satiety}")
        else:
            print(f"У {self.name} немає їжі вдома! Потрібно купити.")
            self.money -= 20
            self.house.food += 30

    def work(self):
        self.money += self.job.salary
        self.satiety -= 15
        print(f"{self.name} попрацював! Зароблено: {self.job.salary} грн.")

    def chill(self):
        self.satiety -= 5
        self.house.mess += 10
        self.pet.play()
        print(f"{self.name} насолоджується життям!")

    def info(self, day):
        print(f"\n--- День {day} ({self.name}) ---")
        print(f"Гроші: {self.money} | Ситість: {self.satiety}")
        print(f"Їжа вдома: {self.house.food} | Безлад: {self.house.mess}")
        print(f"Настрій улюбленця: {self.pet.happiness}")

    def live(self, day):
        self.info(day)
        if self.satiety < 30:
            self.eat()
        elif self.satiety < 50:
            self.work()
        else:
            action = random.randint(1, 2)
            if action == 1:
                self.work()
            else:
                self.chill()


bob = Human(name="Bob")

for day in range(5):
    bob.live(day)
