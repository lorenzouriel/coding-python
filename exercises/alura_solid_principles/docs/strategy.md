O **Strategy** é um **padrão de projeto comportamental** que permite **selecionar algoritmos em tempo de execução**. Ele define uma **família de algoritmos** e encapsula cada um, tornando-os **intercambiáveis** sem alterar o código que os usa.

## Quando usar
* Quando você tem **várias maneiras de realizar uma tarefa** (ex: diferentes formas de ordenação, cálculo, envio).
* Quando quer **desacoplar a lógica de um algoritmo** da classe que o utiliza.
* Para evitar **grandes blocos de `if` ou `match`** baseados em tipo ou estratégia.

## Estrutura
* **Strategy (interface)**: Define o contrato comum entre as estratégias.
* **Concrete Strategies**: Implementam diferentes variações do algoritmo.
* **Context**: Usa uma Strategy para executar o comportamento desejado.

## Exemplo em Python
### Interface da Estratégia
```python
from abc import ABC, abstractmethod

class MetodoEnvio(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass
```

### Estratégias Concretas
```python
class EnvioEmail(MetodoEnvio):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando por e-mail: {mensagem}")

class EnvioSMS(MetodoEnvio):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando por SMS: {mensagem}")

class EnvioPush(MetodoEnvio):
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando notificação push: {mensagem}")
```

### Contexto
```python
class Notificador:
    def __init__(self, estrategia: MetodoEnvio) -> None:
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: MetodoEnvio) -> None:
        self.estrategia = estrategia

    def notificar(self, mensagem: str) -> None:
        self.estrategia.enviar(mensagem)
```

### Uso
```python
notificador = Notificador(EnvioEmail())
notificador.notificar("Pedido confirmado")

notificador.set_estrategia(EnvioSMS())
notificador.notificar("Seu pedido saiu para entrega")
```

## Benefícios
* Facilita a **extensão com novas estratégias**.
* Segue o **princípio Open/Closed**: o código está aberto para extensão, mas fechado para modificação.
* Elimina lógica condicional complexa.

## Cuidados
* Pode gerar muitas **classes pequenas**.
* Pode ser um exagero para **poucas variações simples**.

## Aplicações comuns
* Políticas de desconto
* Algoritmos de ordenação
* Formas de envio de mensagens (como vimos)
* Seleção de rota em apps logísticos
* Cálculo de frete ou imposto