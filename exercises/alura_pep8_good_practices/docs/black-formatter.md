## O que é o Black?
> O **Black** é um *"opinionated code formatter"* para Python. Ele reescreve todo o código com base em regras fixas, sem permitir configurações detalhadas de estilo — **isso é proposital** para evitar discussões e inconsistências.

## Como instalar

Via pip:
```bash
pip install black
```

Via Poetry:
```bash
poetry add --group dev black
```

## Como usar
### 1. Formatando um arquivo específico:
```bash
black nome_do_arquivo.py
```

### 2. Formatando todo o projeto:
```bash
black .
```

### 3. Formatando arquivos selecionados:
```bash
black src/ tests/
```

## Configuração via `pyproject.toml`
O `black` lê configurações do arquivo `pyproject.toml` na raiz do projeto. Exemplo básico:
```toml
[tool.black]
line-length = 88
target-version = ["py311"]
exclude = ["migrations/"]
```

### Principais opções:
| Chave            | Significado                                    |
| ---------------- | ---------------------------------------------- |
| `line-length`    | Tamanho máximo de linha (default: 88)          |
| `target-version` | Versões alvo do Python (`py38`, `py310`, etc.) |
| `include`        | Regex para incluir arquivos (opcional)         |
| `exclude`        | Regex para excluir arquivos/pastas             |

## Dica: Usar com Pre-commit
### 1. Instale o `pre-commit`
```bash
pip install pre-commit
```

### 2. Crie um arquivo `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
```

### 3. Ative os hooks:
```bash
pre-commit install
```

Agora o Black será executado automaticamente **antes de cada commit**.

## O que o Black faz automaticamente?
* Converte aspas simples em duplas (ou vice-versa, se necessário).
* Quebra linhas longas com parênteses.
* Remove espaços desnecessários.
* Formata docstrings.
* Organiza listas, dicionários, chamadas de função com múltiplas linhas.

## Exemplo prático
### Antes:
```python
def soma ( a, b ):
 return a + b
```

### Depois:
```python
def soma(a, b):
    return a + b
```

## Integração com editores
### VS Code
* Instale a extensão **"Python"** e **"Black Formatter"**.
* Adicione no `settings.json`:
```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

## Conclusão
O **Black** automatiza a formatação, melhora a legibilidade e impõe um padrão consistente para todo o projeto, evitando perda de tempo com revisões de estilo. É amplamente adotado em projetos open-source, empresas e times ágeis.