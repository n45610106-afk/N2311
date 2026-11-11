import time
from functools import wraps

def measure_execution_time(func, *args, **kwargs):
    """
    Функція для вимірювання часу виконання іншої функції.
    Повертає кортеж: (результат_функції, час_виконання_в_секундах)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time


def time_it(func):
    """
    Декоратор для вимірювання часу виконання функції.
    Додає до результату виконання час роботи (або друкує його).
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        # Повертаємо результат та час виконання
        return result, execution_time
    return wrapper