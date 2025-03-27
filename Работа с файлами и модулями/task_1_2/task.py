"""Представьте, что вы работаете в компании, занимающейся продажей товаров.
Ваша задача — создать отчет о продажах за неделю в формате CSV.

У вас есть JSON файл, содержащий список словарей, где каждый словарь содержит информацию о товаре:
название, количество проданных единиц и цена за единицу.
Вам нужно сформировать строку для каждой продажи и записать все строки в CSV файл.
"""

import csv
import json

import isort
from utils import get_report_name_with_timestamp


def read_products(filename: str) -> list[str]:
    """

    :param filename: JSON файл с продуктами
    :return: Продукты
    """
    with open(filename) as f:
        products_from_json = json.load(f)

    return products_from_json


def to_csv(filename, product_data):
    """Краткая запись.

    :param filename:
    :param product_data:
    :return:
    """
    with open(filename, "w") as f:
        writer = csv.writer(f)
        headers = ["Название", "Количество", "Цена"]
        writer.writerow(headers)

        for product in product_data:
            writer.writerow(
                (product["name"], product["quantity"], product["unit_price"])
            )


if __name__ == "__main__":  # __main__ исполняйся только в этом файле
    filename = "products.json"
    products = read_products(filename)

    ...

    report_filename = get_report_name_with_timestamp("report.csv")
    to_csv(report_filename, products)
