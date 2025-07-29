# Tratamento de Erros em Python — Guia e Boas Práticas

## 1. Use Exceções para Tratar Erros
* Use `try` / `except` para capturar e tratar exceções que podem ocorrer.
* Evite deixar erros passarem sem tratamento, mas também não abuse de blocos muito amplos.
```python
try:
    resultado = 10 / divisor
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
```

## 2. Capture Exceções Específicas (Evite usar `except:` ou `except Exception:` sem necessidade)
* Capturar erros específicos ajuda a identificar melhor o problema.
```python
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

## 3. Use o bloco `else` para código que deve rodar se não houve erro
```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Divisão inválida")
else:
    print(f"Resultado: {resultado}")
```

## 4. Use o bloco `finally` para liberar recursos (fechar arquivos, conexões)
```python
try:
    arquivo = open("dados.txt")
    dados = arquivo.read()
finally:
    arquivo.close()
```

## 5. Levante (raise) exceções para indicar erros ao chamar funções
* Use `raise` para propagar erros ou criar suas próprias exceções customizadas.
```python
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    return a / b
```

## 6. Crie Exceções Customizadas para sua aplicação
```python
class UsuarioNaoEncontradoError(Exception):
    pass

def buscar_usuario(id):
    if id not in usuarios:
        raise UsuarioNaoEncontradoError(f"Usuário {id} não encontrado")
```

## 7. Use logging em vez de print para registrar erros em produção
```python
import logging

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error(f"Erro ao dividir: {e}")
```

## 8. Em APIs (ex: FastAPI), use exceções HTTP específicas para retornar erros para o cliente
```python
from fastapi import HTTPException

@app.get("/usuario/{id}")
def get_usuario(id: int):
    usuario = buscar_usuario(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
```

## 9. Documente os erros que suas funções podem lançar (ex: docstrings)
```python
def dividir(a, b):
    """
    Divide dois números.

    Raises:
        ValueError: Se o divisor for zero.
    """
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    return a / b
```

## 10. Evite capturar exceções genéricas sem re-raise
Capturar tudo pode esconder erros inesperados:
```python
# Ruim
try:
    ...
except Exception:
    print("Erro")

# Melhor
try:
    ...
except (ValueError, KeyError) as e:
    print(f"Erro esperado: {e}")
```

# Resumo das Boas Práticas
| Prática                         | Descrição                                 |
| ------------------------------- | ----------------------------------------- |
| Capture exceções específicas    | Para saber exatamente qual erro tratar.   |
| Use `else` e `finally`          | Para separar fluxo normal e limpeza.      |
| Use exceções customizadas       | Para deixar o código mais expressivo.     |
| Use `raise` para propagar erros | Para sinalizar problemas para chamadores. |
| Registre erros com `logging`    | Para diagnóstico em produção.             |
| Documente erros nas docstrings  | Facilita entendimento e uso correto.      |
| Não silencie erros inesperados  | Para evitar bugs difíceis de identificar. |