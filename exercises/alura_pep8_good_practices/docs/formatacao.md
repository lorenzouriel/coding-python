## Ordem das Importações segundo a PEP 8

A ordem padrão deve seguir **três grupos distintos**, **separados por uma linha em branco**:
1. **Importações da biblioteca padrão** (built-in)
2. **Importações de bibliotecas de terceiros** (instaladas via pip)
3. **Importações locais do seu projeto**

### Exemplo correto:
```python
# 1. Bibliotecas padrão
import os
import sys

# 2. Bibliotecas de terceiros
from fastapi import FastAPI
from pydantic import BaseModel

# 3. Módulos locais
from app.models.usuario import Usuario
from app.services.usuario_service import criar_usuario
```

## Dicas para Melhorar a Formatação do Código
### 1. Use um formatador automático (recomendado)
* `black`: formata o código automaticamente de forma consistente.
  ```bash
  pip install black
  black .
  ```

### 2. Organize os imports com `isort`
* Ordena e agrupa os imports automaticamente.
  ```bash
  pip install isort
  isort .
  ```

* Para usar junto com o `black`, configure no `pyproject.toml`:
  ```toml
  [tool.isort]
  profile = "black"
  ```

### 3. Siga boas práticas de indentação e espaços
* Use **4 espaços por nível de indentação**.
* Não use espaços desnecessários:
  ```python
  # Correto
  x = 1

  # Errado
  x             =    1
  ```

### 4. Mantenha funções e classes separadas
* Uma linha em branco entre funções relacionadas.
* Duas linhas em branco entre definições de nível superior.
```python
class Usuario:
    ...

def cadastrar_usuario():
    ...
```

### 5. Linhas com no máximo **79 caracteres**
* Quebre linhas longas com `\`, parênteses, colchetes ou chaves.

```python
# Correto
mensagem = (
    "Este é um exemplo de string longa que respeita o limite da PEP 8"
)
```

## Checklist de Ferramentas
| Tarefa                | Ferramenta         |
| --------------------- | ------------------ |
| Formatação automática | `black`, `blue`    |
| Ordenação de imports  | `isort`            |
| Análise de estilo     | `flake8`, `pylint` |
| Tipagem estática      | `mypy`             |
| Docstring PEP 257     | `pydocstyle`       |

## Exemplo antes/depois com `black` e `isort`
### Antes:
```python
import os, sys
from fastapi import FastAPI
from pydantic import BaseModel
from app.services import usuario_service
from app.models import usuario
```

### Depois:
```python
import os
import sys

from fastapi import FastAPI
from pydantic import BaseModel

from app.models import usuario
from app.services import usuario_service
```