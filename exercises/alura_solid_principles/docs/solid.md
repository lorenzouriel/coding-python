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

---

## Alura
### S - Princípio da Responsabilidade Única
Aplicamos este princípio ao garantir que cada classe tivesse uma única responsabilidade. Isso nos permitiu modularizar o código, tornando-o mais legível e fácil de testar. Por exemplo, ao criar classes para diferentes tipos de pedidos, garantimos que cada uma delas tivesse uma função clara e específica.

### O - Princípio Aberto-Fechado
Implementamos o princípio ao projetar o sistema de forma que ele fosse aberto para extensão, mas fechado para modificação. Utilizamos herança e interfaces para permitir que novas funcionalidades fossem adicionadas sem alterar o código existente. Por exemplo, ao adicionar novos tipos de pagamento, fazemos isso estendendo classes base sem modificar diretamente o código original.

### L - Princípio da Substituição de Liskov
Aplicamos esse princípio ao garantir que as subclasses pudessem ser usadas no lugar de suas classes base sem causar erros. Ao implementar a classe base para pagamentos, suas subclasses (como Pagamento com Cartão e Pagamento com Boleto) foram desenhadas para serem intercambiáveis, mantendo a integridade do sistema.

### I - Princípio da Segregação de Interface
Com esse princípio, garantimos que as interfaces fossem específicas e não forçasse implementações desnecessárias. Por exemplo, ao criar diferentes tipos de notificações, as interfaces de envio de notificações foram separadas para que cada tipo (SMS, Email) implementasse apenas o que era necessário para sua funcionalidade.

### D - Princípio da Inversão de Dependência
Esse princípio foi aplicado ao garantir que as classes dependessem de abstrações, e não de implementações concretas. Ao utilizar injeção de dependência, as classes de pagamento, por exemplo, não estavam diretamente acopladas às suas implementações, permitindo flexibilidade e facilitando a manutenção e os testes.

Ao aplicar os princípios SOLID no seu projeto, garantimos um código mais modular, facilitando a manutenção, expansão e entendimento da aplicação. Isso reduz o acoplamento entre as partes do sistema, tornando-o mais resiliente a mudanças, além de incentivar a reutilização de componentes. Assim, construímos uma base sólida para o crescimento do nosso projeto e na melhoria contínua do fluxo de trabalho.