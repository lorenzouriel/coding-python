# List Comprehensions em Python

## O que são?
**List Comprehensions** são uma forma concisa e elegante de criar listas a partir de iteráveis, aplicando transformações e filtros em uma única linha de código.

Em vez de usar um `for` tradicional e `append` para construir listas, você pode usar uma expressão mais legível e rápida.

## Sintaxe básica
```python
[nova_expressao for item in iteravel if condicao]
```

* `nova_expressao`: como você quer transformar o `item`.
* `item`: variável que recebe cada elemento do iterável.
* `iteravel`: qualquer objeto iterável (lista, tupla, range, etc.).
* `if condicao` (opcional): filtro para incluir só alguns elementos.

## Exemplos
### Exemplo 1 — Criar uma lista com os quadrados de números de 0 a 9
```python
quadrados = [x**2 for x in range(10)]
print(quadrados)
# Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Exemplo 2 — Filtrar apenas números pares e elevar ao quadrado
```python
pares_quadrado = [x**2 for x in range(10) if x % 2 == 0]
print(pares_quadrado)
# Saída: [0, 4, 16, 36, 64]
```

### Exemplo 3 — Converter uma lista de strings para minúsculas
```python
nomes = ["Ana", "Bruno", "Carlos"]
nomes_minusculos = [nome.lower() for nome in nomes]
print(nomes_minusculos)
# Saída: ['ana', 'bruno', 'carlos']
```

### Exemplo 4 — Compreensão aninhada (listas dentro de listas)
```python
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matriz)
# Saída: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## Quando usar List Comprehensions?
* Para criar listas simples e expressar transformações/filtros de forma clara.
* Quando a lógica couber em uma linha e for facilmente legível.

## Quando evitar?
* Se a lógica for muito complexa ou envolver várias etapas, prefira usar loops tradicionais.
* Para estruturas muito aninhadas, que dificultam a leitura.

## Dica para leitura e manutenção
Se a expressão ficar muito longa, use parênteses e quebre em várias linhas:

```python
resultados = [
    x**2
    for x in range(20)
    if x % 2 == 0
]
```