# Clean Code
As boas práticas de **Clean Code em Python** ajudam a escrever um código mais **legível**, **manutenível** e **escalável**. Abaixo estão os principais princípios, organizados por categoria:

## 1. **Nomenclatura Clara e Descritiva**
Use nomes que expressem *intenção*.

**Bom:**
```python
def calcular_total_com_imposto(valor, taxa_imposto):
    ...
```

**Ruim:**
```python
def calc(v, t):
    ...
```

## 2. **Funções Pequenas e Focadas**
Cada função deve fazer **apenas uma coisa**.

**Bom:**
```python
def buscar_usuario_por_id(id): ...
def formatar_usuario(usuario): ...
```

**Ruim:**
```python
def processar_usuario(id):
    # busca, formata, salva e envia e-mail
```

## 3. **Evite Comentários Desnecessários**
Comente apenas o **que** é difícil de entender, e não o óbvio.

**Bom:**
```python
# Evita divisão por zero
if denominador == 0:
    return None
```

**Ruim:**
```python
# Soma dois números
soma = a + b
```

## 4. **Evite Código Morto ou Não Utilizado**
Mantenha o código limpo de:
* Variáveis não utilizadas
* Funções não chamadas
* `print()` em produção

## 5. **Use Tipagem com `type hints`**

Ajuda na legibilidade, autocompletar e verificação estática.

**Bom:**
```python
def enviar_email(destinatario: str, assunto: str, corpo: str) -> bool:
    ...
```

## 6. **Evite Números Mágicos e Strings Literais**
Use constantes nomeadas.
**Bom:**
```python
TAXA_IMPOSTO = 0.15
if preco > 1000 * TAXA_IMPOSTO:
    ...
```

## 7. **Divida em Módulos**
Não coloque tudo em um único arquivo. Separe por domínio:
```
/app
  ├── models.py
  ├── services.py
  ├── controllers.py
  ├── schemas.py
```

## 8. **Trate Erros com Elegância**
Use `try/except` corretamente, nunca silencie erros sem necessidade.

**Bom:**
```python
try:
    resultado = operacao()
except ValueError as e:
    logger.error(f"Erro ao processar: {e}")
    raise
```

## 9. **Evite Código Duplicado**
Se copiar/colar mais de 2 vezes, abstraia para uma função.

## 10. **Use List Comprehensions com Clareza**

**Bom:**
```python
nomes = [cliente.nome for cliente in clientes if cliente.ativo]
```

**Ruim:**
```python
nomes = []
for cliente in clientes:
    if cliente.ativo:
        nomes.append(cliente.nome)
```

## 11. **Documente com Docstrings**

**Bom:**
```python
def somar(a: int, b: int) -> int:
    """Retorna a soma de dois números inteiros."""
    return a + b
```

## 12. **Use Linters e Formatadores**

Ferramentas como:
* [`black`](https://github.com/psf/black): formata o código
* [`flake8`](https://flake8.pycqa.org/): checa padrões de estilo
* [`mypy`](http://mypy-lang.org/): checa tipos
* [`isort`](https://pycqa.github.io/isort/): organiza imports


## 13. **Prefira Classes Simples com Pydantic ou Dataclasses**
**Bom:**
```python
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float
```

## 14. **Use `enumerate`, `zip`, `any`, `all`, etc.**
**Exemplo:**
```python
for i, valor in enumerate(lista):
    ...
```

## 15. **Siga a PEP 8**
É o guia oficial de estilo Python. Use:
```bash
python -m pep8 nome_do_arquivo.py
```
