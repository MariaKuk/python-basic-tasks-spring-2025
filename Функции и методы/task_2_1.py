"""Поиск товаров с определенным размером скидки

Напишите функцию, которая принимает словарь,
содержащий название продукта и скидку в качестве ключа и значения соответственно. ,

Функция должна вернуть  товаров, имеющих скидку не меньше заданной.

Функция должна найти и вернуть в новом словаре только те продукты,
у которых размер скидки не меньше заданного значения.
"""

discount_products = {
    "яблоко": 10,
    "банан": 5,
    "молоко": 20,
    "хлеб": 0,
    "сыр": 15,
}


def filter_discount_product(products, discount):
    filter_products = {}

    for (
        product,
        current_discount,
    ) in products.items():  # Перебераю по порядку пары ключ-значение
        if current_discount >= discount:  # если скидка не меньше заданной
            filter_products[product] = (
                current_discount  # В новый словарь добавляю элемент
            )

    return filter_products


print(filter_discount_product(discount_products, 20))
