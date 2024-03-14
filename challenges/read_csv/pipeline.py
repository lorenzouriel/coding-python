import csv

path_archive = "C:\Portfolio\projects\coding-python\challenges/read_csv/vendas.csv"

def read_csv(csv_file_name: str) -> list[dict]:
    """
    Function that reads csv and return a list of dictionaires
    """
    list = []
    with open(csv_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line in reader:
            list.append(line)
    return list


def filter_not_deliver_products(lists: list[dict]) -> list[dict]:
    """
    Function that filter products not delivered: entrega = True
    """
    filter_list_products = []
    for product in lists:
        if product.get("entregue") == "True":
            filter_list_products.append(product)
    return filter_list_products


def sum_products_values(lists: list[dict]) -> int:
    """
    Function that sum products values
    """
    total_value = 0
    for product in lists:
        total_value += int(product.get("price"))
    return total_value