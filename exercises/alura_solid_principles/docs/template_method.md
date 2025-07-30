O **Template Method** é um *padrão de projeto comportamental* que define o **esqueleto de um algoritmo** numa classe base, permitindo que **subclasses sobrescrevam partes específicas** do processo **sem alterar sua estrutura geral**.

## Quando Usar
* Quando você tem **um processo com etapas fixas**, mas que podem variar parcialmente dependendo da situação.
* Para evitar **duplicação de código** entre classes com processos semelhantes.
* Para permitir **reuso e especialização controlada**.

## Conceito
A classe base define um **método template** com a estrutura geral do algoritmo. Algumas etapas são implementadas nela, enquanto outras são deixadas como métodos abstratos (ou *hooks*) para subclasses especializarem.

## Exemplo em Python
### Classe Base com Template Method:
```python
from abc import ABC, abstractmethod

class ProcessoPedido(ABC):
    def processar(self):
        self.validar_pedido()
        self.processar_pagamento()
        self.enviar_confirmacao()

    def validar_pedido(self):
        print("Validando o pedido...")

    @abstractmethod
    def processar_pagamento(self):
        pass

    def enviar_confirmacao(self):
        print("Enviando e-mail de confirmação.")
```

### Subclasse 1: Pagamento com Cartão
```python
class PedidoCartao(ProcessoPedido):
    def processar_pagamento(self):
        print("Processando pagamento com cartão de crédito.")
```

### Subclasse 2: Pagamento com Pix
```python
class PedidoPix(ProcessoPedido):
    def processar_pagamento(self):
        print("Processando pagamento com Pix.")
```

### Uso:
```python
pedido = PedidoCartao()
pedido.processar()

# Output:
# Validando o pedido...
# Processando pagamento com cartão de crédito.
# Enviando e-mail de confirmação.
```

## Variações
Você pode definir **métodos hook** opcionais:
```python
class ProcessoPedido(ABC):
    def processar(self):
        self.validar_pedido()
        self.processar_pagamento()
        self.enviar_confirmacao()
        self.log_extra()

    def log_extra(self):  # Hook: opcional
        pass
```

## Vantagens
* Reduz **duplicação** de código.
* Facilita a **reutilização** da estrutura comum.
* Segue o princípio **Open/Closed (OCP)** do SOLID.

## Desvantagens
* Pode aumentar a **complexidade** da hierarquia de classes.
* Não é ideal se as etapas forem muito **variáveis entre si**.