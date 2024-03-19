from etl import read_csv, filter_not_deliver_products, sum_products_values

path_archive = "C:\Portfolio\projects\coding-python\challenges/read_csv/vendas.csv"

products_list = read_csv(path_archive)
deliver_products = filter_not_deliver_products(products_list)
total_value_of_delivery_products = sum_products_values(deliver_products)

print(products_list)
print(deliver_products)
print(total_value_of_delivery_products)