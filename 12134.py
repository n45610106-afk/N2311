import colorama
import inspect

# Інтроспекція бібліотеки colorama
print("Назва бібліотеки:", colorama.__name__)
print("Опис бібліотеки:", colorama.__doc__)

# Основні атрибути
print("\nОсновні атрибути:")
print(dir(colorama))

# Інформація про основні класи
print("\nКлас Fore:")
print(dir(colorama.Fore))

print("\nКлас Back:")
print(dir(colorama.Back))

print("\nКлас Style:")
print(dir(colorama.Style))

# Рекомендації щодо використання
print("\nРекомендації:")
print("Fore — змінює колір тексту.")
print("Back — змінює колір фону.")
print("Style — змінює стиль тексту.")
print("init() — ініціалізує бібліотеку.")
print("deinit() — завершує її роботу.")