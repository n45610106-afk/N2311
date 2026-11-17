import tkinter as tk
from tkinter import messagebox
import requests


class CurrencyConverter:
    """Конвертер гривны в доллары США по официальному курсу НБУ."""

    def __init__(self):
        self.url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        self.usd_rate = self._parse_usd_rate()

    def _parse_usd_rate(self) -> float:
        """Получает официальный курс USD через API НБУ."""

        response = requests.get(self.url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data or "rate" not in data[0]:
            raise ValueError("Не удалось получить курс доллара.")

        return float(data[0]["rate"])

    def uah_to_usd(self, amount_uah: float) -> float:
        """Конвертирует гривны в доллары."""

        if amount_uah < 0:
            raise ValueError("Сумма не может быть отрицательной.")

        return amount_uah / self.usd_rate


class ConverterApp:
    """Графический интерфейс Tkinter."""

    def __init__(self, root: tk.Tk, converter: CurrencyConverter):
        self.root = root
        self.converter = converter

        self.root.title("Конвертер валют (НБУ)")
        self.root.geometry("380x230")
        self.root.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        rate_text = (
            f"Официальный курс НБУ:\n"
            f"1 USD = {self.converter.usd_rate:.4f} UAH"
        )

        tk.Label(
            self.root,
            text=rate_text,
            font=("Arial", 10, "bold"),
            fg="#1f4e78"
        ).pack(pady=(15, 10))

        tk.Label(
            self.root,
            text="Введите сумму в гривнах (UAH):",
            font=("Arial", 10)
        ).pack()

        self.entry_uah = tk.Entry(
            self.root,
            font=("Arial", 12),
            justify="center",
            width=22
        )
        self.entry_uah.pack(pady=5)
        self.entry_uah.focus()

        self.root.bind("<Return>", lambda event: self.calculate())

        tk.Button(
            self.root,
            text="Конвертировать в USD",
            font=("Arial", 10, "bold"),
            bg="#2e7d32",
            fg="white",
            cursor="hand2",
            command=self.calculate
        ).pack(pady=10)

        self.result_label = tk.Label(
            self.root,
            text="Результат: 0.00 USD",
            font=("Arial", 12, "bold")
        )
        self.result_label.pack(pady=5)

    def calculate(self):
        raw_value = self.entry_uah.get().strip().replace(",", ".")

        try:
            amount_uah = float(raw_value)

            if amount_uah < 0:
                raise ValueError("Сумма не может быть отрицательной.")

            amount_usd = self.converter.uah_to_usd(amount_uah)

            self.result_label.config(
                text=f"Результат: {amount_usd:.2f} USD",
                fg="#000000"
            )

        except ValueError as e:
            messagebox.showerror(
                "Ошибка ввода",
                f"Введите корректное неотрицательное число.\n{e}"
            )


def main():
    try:
        converter = CurrencyConverter()

    except Exception as e:
        temp_root = tk.Tk()
        temp_root.withdraw()

        messagebox.showerror(
            "Ошибка подключения",
            f"Не удалось получить курс НБУ:\n{e}"
        )

        temp_root.destroy()
        return

    root = tk.Tk()
    app = ConverterApp(root, converter)
    root.mainloop()


if __name__ == "__main__":
    main()