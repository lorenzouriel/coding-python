from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("Lorenzo", "Rua das Flores, 123")
item_um = Item("Notebook", 2500.00)
item_dois = Item("Mouse", 150.00)

itens = [item_um, item_dois]

taxa_entrega: float = 10.00
pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

total_retirada = pedido_retirada.calcular_total()
total_delivery = pedido_delivery.calcular_total()

print(f"Total de Retirada {total_retirada:.2f} e Total de Delivery {total_delivery:.2f}")