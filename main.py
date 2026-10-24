class Student:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.year = 1

    def work(self):
        self.money += 1000
        print(f"{self.name} пішов на роботу і заробив 1000 грн.")

    def study(self):
        print(f"{self.name} займається навчанням.")

    def spend_money(self):
        if self.money >= 500:
            self.money -= 500
            print(f"{self.name} витратив 500 грн на відпочинок.")
        else:
            print(f"{self.name} не вистачає грошей. Потрібно піти на роботу.")
            self.work()

    def live_year(self):
        print(f"\nСтудент {self.name} починає проживати рік.")

        for month in range(1, 13):
            print(f"\nМісяць {month}")

            if self.money < 500:
                self.work()

            self.study()
            self.spend_money()

        self.year += 1
        print(f"\nРік завершено! Залишилося грошей: {self.money} грн.")
        print(f"Студент перейшов на {self.year} курс.")


student = Student("Андрій", 2000)
student.live_year()
#друге завдання