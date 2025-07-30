from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus

cliente = Cliente("Lorenzo", "Waves For Me")
item_um = Item("Camiseta Waves", 49.90)
item_dois = Item("Calça Waves", 89.90)
itens = [item_um, item_dois]

taxa_entrega = 10.00
pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = "O pagamento foi confirmado!"
MENSAGEM_PREPARANDO = "O pedido está sendo preparado!"
MENSAGEM_ENVIADO = "O pedido saiu para a entrega!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observador(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO