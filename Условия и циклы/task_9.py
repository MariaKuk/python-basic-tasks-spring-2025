"""Поиск продукта с наибольшими расходами

Представьте, что вы ведете учет своих расходов на различные продукты в течение недели.
У вас есть список покупок, где каждый элемент представляет собой кортеж, содержащий название продукта и его цену.
Вы хотите узнать, на какой продукт было потрачено наибольшее количество денег за неделю.

Напишите программу, которая:

1. Имеет список покупок за неделю, где каждый элемент - это кортеж вида (продукт, цена).
2. Находит продукт, на который было потрачено наибольшее количество денег.
3. Выводит название этого продукта и общую сумму, потраченную на него.
"""

purchases = [
    ("яблоко", 50),
    ("банан", 30),
    ("яблоко", 50),
    ("молоко", 70),
    ("хлеб", 40),
    ("банан", 30),
    ("яблоко", 50),
    ("молоко", 70),
    ("сыр", 100),
    ("яблоко", 50),
]

total_expenses = {}  # Общие затраты
for product, expense in purchases:
    # product = item[0]
    # expense = item[1]

    if product not in total_expenses:
        total_expenses[product] = expense
    else:
        total_expenses[product] += expense

print(total_expenses)

min_expense_product = None
min_expense = float("inf")
for product in total_expenses:  # только ключи
    expense = total_expenses[product]

    if expense < min_expense:
        min_expense = expense
        min_expense_product = product

print(f"На товар {min_expense_product} потрачено меньше всего денег = {min_expense}")
