"""Написать свою реализацию функции `enumerate`.

Итерируемые объекты:
- кортежи
- списки
- строки
- множества
- словари
"""

if __name__ == "__main__":
    collection = ("a", "b", "c")
    for i, value in enumerate(collection):
        print(f"Индекс: {i} | Значение: {value}")

    print("---")

    for pos, value in enumerate(collection, 1):
        print(f"Позиция: {pos} | Значение: {value}")
