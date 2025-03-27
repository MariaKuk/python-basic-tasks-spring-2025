"""Расчет цен продуктов с учетом скидки

Напишите функцию, которая принимает список словарей, содержащий название продукта, его цену и скидку.
Функция должна вернуть список цен с учетом скидки.

Каждый словарь в списке содержит следующие ключи:
- `name`: название продукта (строка)
- `price`: цена продукта (число)
- `discount`: скидка на продукт в процентах (число)

Функция должна рассчитать новую цену для каждого продукта с учетом скидки и вернуть список этих новых цен.
"""

products = [
    {"name": "яблоко", "price": 100, "discount": 10},
    {"name": "банан", "price": 200, "discount": 5},
    {"name": "молоко", "price": 150, "discount": 20},
    {"name": "хлеб", "price": 50, "discount": 0},
    {"name": "сыр", "price": 300, "discount": 15},
]


def get_discount_price(products_):
    list_price = []
    for product in products_:  # product - словарь
        price_with_discount = product["price"] * (1 - product["discount"] * 0.01)
        list_price.append(price_with_discount)

    return list_price


print(get_discount_price(products))
