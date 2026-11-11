import functools


def safe_calculator(func):
    @functools.wraps(func)
    def wrapper(expression, *args, **kwargs):
        # Перевіряємо, чи передано саме рядок
        if not isinstance(expression, str):
            print(f"Помилка: Вираз має бути рядком (тип str), а передано {type(expression).__name__}.")
            return None

        try:
            # Обчислюємо результат за допомогою оригінальної функції
            return func(expression, *args, **kwargs)
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль неможливе.")
            return None
        except SyntaxError:
            print(f"Помилка синтаксису: Некоректний математичний вираз '{expression}'.")
            return None
        except NameError:
            print(f"Помилка: Вираз '{expression}' містить невідомі змінні або букви.")
            return None
        except Exception as e:
            print(f"Виникла непередбачена помилка: {e}")
            return None

    return wrapper


# Застосовуємо декоратор до початкової функції
@safe_calculator
def calculate(expression):
    return eval(expression)


# --- Приклади використання ---
if __name__ == "__main__":
    print("Успішне обчислення:", calculate("2 + 2 * 2"))  # 6
    print("Ділення на нуль:", calculate("10 / 0"))  # Повідомлення про помилку -> None
    print("Некоректний синтаксис:", calculate("2 ++ "))  # Повідомлення про помилку -> None
    print("Спроба виконати код/букви:", calculate("abc"))  # Повідомлення про помилку -> None