[LEIA MAIS AQUI](https://www.alura.com.br/artigos/design-patterns-python?utm_source=gnarus&utm_medium=timeline)

## 1. Factory Method
### Objetivo
Encapsular a criação de objetos, permitindo que subclasses decidam qual classe instanciar. Isso reduz o acoplamento entre o código cliente e as classes concretas.

### Estrutura
* Uma interface ou classe abstrata define um método de criação (`factory_method`)
* Subclasses concretas implementam esse método para instanciar objetos diferentes

### Exemplo

```python
from abc import ABC, abstractmethod

# Produto
class Documento(ABC):
    @abstractmethod
    def gerar(self) -> str:
        pass

# Produtos concretos
class PDF(Documento):
    def gerar(self):
        return "Documento PDF gerado"

class Word(Documento):
    def gerar(self):
        return "Documento Word gerado"

# Fábrica
class CriadorDocumento(ABC):
    @abstractmethod
    def criar_documento(self) -> Documento:
        pass

# Fábricas concretas
class CriadorPDF(CriadorDocumento):
    def criar_documento(self):
        return PDF()

class CriadorWord(CriadorDocumento):
    def criar_documento(self):
        return Word()

# Uso
criador = CriadorPDF()
doc = criador.criar_documento()
print(doc.gerar())
```

## 2. Template Method
### Objetivo
Definir o esqueleto de um algoritmo em uma classe base, permitindo que subclasses implementem etapas específicas.

### Exemplo
```python
from abc import ABC, abstractmethod

class Receita(ABC):
    def preparar(self):
        self.aquecer()
        self.adicionar_ingredientes()
        self.cozinhar()
        self.servir()

    def aquecer(self):
        print("Aquecendo a panela")

    @abstractmethod
    def adicionar_ingredientes(self):
        pass

    def cozinhar(self):
        print("Cozinhando")

    def servir(self):
        print("Servindo o prato")

class Omelete(Receita):
    def adicionar_ingredientes(self):
        print("Adicionando ovos e temperos")

class Macarrao(Receita):
    def adicionar_ingredientes(self):
        print("Adicionando macarrão e molho")

# Uso
receita = Omelete()
receita.preparar()
```

## 3. Strategy
### Objetivo
Permitir a escolha de um algoritmo em tempo de execução. A lógica é isolada em diferentes classes que implementam a mesma interface.

### Exemplo
```python
from abc import ABC, abstractmethod

# Interface da estratégia
class FreteStrategy(ABC):
    @abstractmethod
    def calcular(self, peso: float) -> float:
        pass

class FreteSEDEX(FreteStrategy):
    def calcular(self, peso: float) -> float:
        return peso * 1.5

class FretePAC(FreteStrategy):
    def calcular(self, peso: float) -> float:
        return peso * 0.9

# Contexto
class CalculadoraFrete:
    def __init__(self, strategy: FreteStrategy):
        self.strategy = strategy

    def calcular_frete(self, peso: float) -> float:
        return self.strategy.calcular(peso)

# Uso
calculadora = CalculadoraFrete(FretePAC())
print("Valor do frete:", calculadora.calcular_frete(10))
```

## 4. Facade
### Objetivo
Ocultar a complexidade de um subsistema fornecendo uma interface unificada mais simples.

### Exemplo
```python
class Autenticacao:
    def autenticar(self):
        print("Usuário autenticado")

class Pagamento:
    def realizar_pagamento(self):
        print("Pagamento efetuado")

class Notificacao:
    def enviar_email(self):
        print("E-mail enviado")

# Fachada
class LojaOnline:
    def __init__(self):
        self.auth = Autenticacao()
        self.pagamento = Pagamento()
        self.email = Notificacao()

    def processar_compra(self):
        self.auth.autenticar()
        self.pagamento.realizar_pagamento()
        self.email.enviar_email()
        print("Compra finalizada com sucesso")

# Uso
loja = LojaOnline()
loja.processar_compra()
```

## 5. Observer
### Objetivo
Permitir que múltiplos objetos se inscrevam em um objeto sujeito, sendo notificados quando ele muda de estado.

### Exemplo
```python
from abc import ABC, abstractmethod
from typing import List

# Observer
class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass

class Usuario(Observer):
    def __init__(self, nome: str):
        self.nome = nome

    def atualizar(self, mensagem: str):
        print(f"{self.nome} recebeu: {mensagem}")

# Sujeito (Subject)
class Canal:
    def __init__(self):
        self.inscritos: List[Observer] = []

    def inscrever(self, observer: Observer):
        self.inscritos.append(observer)

    def notificar(self, mensagem: str):
        for inscrito in self.inscritos:
            inscrito.atualizar(mensagem)

    def novo_video(self, titulo: str):
        print("Novo vídeo:", titulo)
        self.notificar(f"Assista agora: {titulo}")

# Uso
canal = Canal()
canal.inscrever(Usuario("Lucas"))
canal.inscrever(Usuario("Ana"))
canal.novo_video("Introdução ao Python")
```

# Comparação Geral
| Padrão          | Uso Principal                                   |
| --------------- | ----------------------------------------------- |
| Factory Method  | Instanciar objetos com flexibilidade            |
| Template Method | Reutilizar estrutura de algoritmos com variação |
| Strategy        | Encapsular algoritmos intercambiáveis           |
| Facade          | Simplificar subsistemas complexos               |
| Observer        | Reagir a eventos de outro objeto                |