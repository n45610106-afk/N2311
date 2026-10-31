import random


class Cipher:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        operation = random.choice(["+", "-", "*"])

        if operation == "+":
            result = self.__a + self.__b
        elif operation == "-":
            result = self.__a - self.__b
        else:
            result = self.__a * self.__b

        return f"Результат обчислення: {result}"


obj = Cipher(10, 5)

print(obj)
