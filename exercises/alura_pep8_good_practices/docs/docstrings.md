## Sintaxe básica
As docstrings em Python são strings de documentação escritas logo após a definição de módulos, funções, métodos ou classes, e servem para explicar o que aquele bloco de código faz. Elas são fundamentais para entendimento, manutenção e geração automática de documentação (ex: com Sphinx, MkDocs).

Docstrings devem usar **aspas triplas** (`""" """` ou `''' '''`) e ficam **logo após a definição** da função, classe ou módulo.
```python
def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada para o nome fornecido."""
    return f"Olá, {nome}!"
```

## Acesso à docstring
Você pode acessar a docstring em tempo de execução via `.__doc__`:
```python
print(saudacao.__doc__)
```

## Padrões de escrita de docstrings
Há diferentes **convenções** para escrever docstrings. As mais comuns são:

### 1. **PEP 257** (guia oficial)
* Simples, direta e curta.
* Frase em **forma imperativa**.
* Primeira linha resume o propósito.
* Linhas seguintes (opcional) dão mais contexto.
```python
def soma(a: int, b: int) -> int:
    """Soma dois números inteiros e retorna o resultado."""
    return a + b
```

### 2. **Google Style**
Formato muito usado em projetos modernos.
```python
def dividir(a: float, b: float) -> float:
    """Divide dois números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Resultado da divisão.

    Raises:
        ZeroDivisionError: Se o divisor for zero.
    """
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
```

### 3. **NumPy/SciPy Style**
```python
def multiplicar(a: int, b: int) -> int:
    """
    Multiplica dois números.

    Parameters
    ----------
    a : int
        O primeiro número.
    b : int
        O segundo número.

    Returns
    -------
    int
        O produto de a e b.
    """
    return a * b
```

## Ferramentas para validar docstrings
* [`pydocstyle`](https://pypi.org/project/pydocstyle/): Verifica se as docstrings seguem o PEP 257.
* `flake8-docstrings`: Plugin para o `flake8` que valida as docstrings.
* `interrogate`: Verifica se as funções e classes têm docstrings (sem avaliar o conteúdo).
```bash
pip install pydocstyle
pydocstyle caminho/do/projeto/
```

## Boas práticas
✔ Sempre escreva docstrings para **funções públicas** e **classes**.
✔ Seja objetivo: explique o “**o quê**” e “**por quê**” e não “**como**”.
✔ Comece com letra **maiúscula** e termine sem ponto final se for só uma linha.
✔ Use estilo consistente (Google, NumPy ou PEP 257).

## Exemplo completo com classe
```python
class Calculadora:
    """Classe para operações matemáticas simples."""

    def __init__(self):
        """Inicializa uma instância da calculadora."""
        self.resultado = 0

    def somar(self, a: int, b: int) -> int:
        """Soma dois números inteiros.

        Args:
            a (int): Primeiro número.
            b (int): Segundo número.

        Returns:
            int: Resultado da soma.
        """
        self.resultado = a + b
        return self.resultado
```
