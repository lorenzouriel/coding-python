Os **princípios SOLID** são cinco diretrizes fundamentais do design de software orientado a objetos. Eles ajudam a escrever código **mais limpo, flexível e fácil de manter**. A sigla representa:

## S — Single Responsibility Principle (Princípio da Responsabilidade Única)
> Uma classe deve ter apenas **uma única razão para mudar**.

**Ruim:**
```python
class Usuario:
    def salvar(self):
        ...
    def enviar_email_boas_vindas(self):
        ...
```

**Melhor:**
```python
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class UsuarioRepository:
    def salvar(self, usuario: Usuario):
        ...

class EmailService:
    def enviar_boas_vindas(self, email: str):
        ...
```

## O — Open/Closed Principle (Aberto para Extensão, Fechado para Modificação)
> Classes devem estar **abertas para extensão**, mas **fechadas para modificação**.

**Ruim:**
```python
def calcular_desconto(tipo_cliente, valor):
    if tipo_cliente == "vip":
        return valor * 0.9
    elif tipo_cliente == "premium":
        return valor * 0.8
```

**Melhor (com polimorfismo):**
```python
class Desconto:
    def calcular(self, valor: float) -> float:
        return valor

class DescontoVip(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.9

class DescontoPremium(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.8
```

## L — Liskov Substitution Principle (Princípio da Substituição de Liskov)
> Subclasses devem poder **substituir suas superclasses** sem quebrar o programa.

**Ruim:**
```python
class Pato:
    def voar(self):
        print("Voando")

class PatoDeBorracha(Pato):
    def voar(self):
        raise Exception("Pato de borracha não voa")
```

**Melhor:**
```python
class Ave:
    def emitir_som(self):
        ...

class AveVoadora(Ave):
    def voar(self):
        ...

class Pato(AveVoadora):
    ...

class PatoDeBorracha(Ave):
    def emitir_som(self):
        print("Quack!")
```


## I — Interface Segregation Principle (Princípio da Segregação de Interfaces)
> Uma classe não deve ser forçada a depender de métodos que **não utiliza**.

**Ruim (interface gorda):**
```python
class Animal:
    def voar(self): ...
    def nadar(self): ...
    def correr(self): ...
```

**Melhor:**
```python
class Voador:
    def voar(self): ...

class Nadador:
    def nadar(self): ...

class Ave(Voador):
    ...

class Peixe(Nadador):
    ...
```

## D — Dependency Inversion Principle (Princípio da Inversão de Dependência)
> **Dependa de abstrações**, não de implementações concretas.

**Ruim:**
```python
class MySQLRepositorio:
    def salvar(self, dados): ...

class Servico:
    def __init__(self):
        self.repositorio = MySQLRepositorio()
```

**Melhor:**
```python
class Repositorio:
    def salvar(self, dados): ...

class MySQLRepositorio(Repositorio):
    def salvar(self, dados): ...

class Servico:
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio
```

## Resumo em Tabela
| Princípio | Descrição                                         |
| --------- | ------------------------------------------------- |
| **S**     | Uma classe, uma responsabilidade                  |
| **O**     | Pode ser estendido sem alterar código existente   |
| **L**     | Substitutos devem se comportar como a superclasse |
| **I**     | Evite interfaces grandes e genéricas              |
| **D**     | Dependa de abstrações, não de implementações      |