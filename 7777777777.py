import sqlite3
import time
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class KremenchukWeatherMonitor:
    """Клас для парсингу погоди у Кременчуці та збереження даних у БД SQLite."""

    def __init__(
        self,
        url: str = "https://sinoptik.ua/pohoda/kremenchuk",
        db_name: str = "kremenchuk_weather.db",
    ):
        self.url = url
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        """Створює базу даних та таблицю для збереження погоди."""

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS weather (
                    date_time TEXT NOT NULL,
                    temperature TEXT NOT NULL
                )
                """
            )

            conn.commit()

    def get_current_temperature(self) -> str:
        """Отримує поточну температуру повітря у Кременчуці."""

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            self.url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Шукаємо значення температури, наприклад +6°C або -2°
        for tag in soup.find_all(["p", "span", "div"]):
            text = tag.get_text(strip=True)

            if re.fullmatch(r"[+-]?\d+\s*°[CС]?", text):
                return text

        raise ValueError(
            "Не вдалося знайти значення температури на сторінці."
        )

    def save_to_db(self, date_time: str, temperature: str):
        """Зберігає дату, час та температуру у базі даних."""

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO weather (date_time, temperature)
                VALUES (?, ?)
                """,
                (date_time, temperature),
            )

            conn.commit()

    def run(self, interval_minutes: int = 30):
        """Запускає моніторинг погоди з заданим інтервалом."""

        if interval_minutes <= 0:
            raise ValueError("Інтервал повинен бути більшим за нуль.")

        print(
            f"Моніторинг погоди у Кременчуці запущено "
            f"(інтервал: {interval_minutes} хв)."
        )

        print(
            "Для зупинки натисніть Ctrl+C або кнопку Stop у PyCharm.\n"
        )

        try:
            while True:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                try:
                    temp = self.get_current_temperature()

                    self.save_to_db(now, temp)

                    print(
                        f"[{now}] Збережено в БД: "
                        f"температура у Кременчуці = {temp}"
                    )

                except Exception as e:
                    print(
                        f"[{now}] Помилка під час отримання "
                        f"або запису даних: {e}"
                    )

                time.sleep(interval_minutes * 60)

        except KeyboardInterrupt:
            print("\nСканування зупинено користувачем.")


if __name__ == "__main__":
    monitor = KremenchukWeatherMonitor()
    monitor.run(interval_minutes=30)