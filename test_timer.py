import unittest
import time
from timer import measure_execution_time, time_it


# Тестові функції для перевірки
def dummy_sleep_function(seconds):
    time.sleep(seconds)
    return "Done"


@time_it
def decorated_sleep_function(seconds):
    time.sleep(seconds)
    return "Decorated Done"


class TestExecutionTime(unittest.TestCase):

    def test_measure_execution_time(self):
        sleep_duration = 0.1
        result, exec_time = measure_execution_time(dummy_sleep_function, sleep_duration)

        # Перевіряємо результат виконання функції
        self.assertEqual(result, "Done")
        # Перевіряємо, що виміряний час приблизно дорівнює затримці
        self.assertAlmostEqual(exec_time, sleep_duration, delta=0.03)

    def test_decorator_execution_time(self):
        sleep_duration = 0.15
        result, exec_time = decorated_sleep_function(sleep_duration)

        # Перевіряємо результат
        self.assertEqual(result, "Decorated Done")
        # Перевіряємо точність часу виконання декоратора
        self.assertAlmostEqual(exec_time, sleep_duration, delta=0.03)


if __name__ == '__main__':
    unittest.main()