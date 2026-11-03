result = []

def divider(a, b):
    if a < b:
        raise ValueError("ValueError: a менше b")

    if b > 100:
        raise IndexError("IndexError: b більше 100")

    return a / b


data = {
    10: 2,
    2: 5,
    "123": 4,
    18: 0,
    (1, 2): 15,
    150: 101,
    8: 4
}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
        print("Результат:", res)

    except Exception as error:
        print("Виникла помилка:", type(error).__name__, "-", error)

print("\nУспішні результати:", result)