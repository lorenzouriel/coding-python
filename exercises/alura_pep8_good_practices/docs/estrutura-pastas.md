# **Estrutura de Pastas**
## 1. `src/` ou `src/app/`
* **Objetivo:** Contém o código-fonte principal da aplicação.
* **Organização sugerida:**
  ```bash
  src/
  └── app/
      ├── main.py              # Ponto de entrada da aplicação
      ├── models/              # Modelos Pydantic ou ORM
      ├── routers/             # Endpoints (FastAPI)
      ├── services/            # Lógica de negócio
      ├── core/                # Configurações globais (ex: database, env, auth)
      ├── utils/               # Funções utilitárias
      └── __init__.py
  ```

## 2. `tests/`
* **Objetivo:** Armazena testes automatizados (unitários, integração, etc.).
* **Ferramentas sugeridas:** `pytest`, `unittest`, `coverage`.

## 3. `docs/`
* **Objetivo:** Contém a documentação técnica do projeto, podendo ser gerada com ferramentas como `Sphinx`, `MkDocs`, ou `Docusaurus`.

## 4. `scripts/`
* **Objetivo:** Scripts auxiliares para instalação, deploy, geração de dados, execução de testes, entre outros.

# **Arquivos Comuns**
| Arquivo                   | Função                                                                 |
| ------------------------- | ---------------------------------------------------------------------- |
| `.gitignore`              | Arquivos e pastas ignoradas pelo Git.                                  |
| `README.md`               | Apresentação do projeto: descrição, uso, instalação, exemplos.         |
| `.pre-commit-config.yaml` | Configuração de hooks de pré-commit para garantir qualidade do código. |
| `.python-version`         | Especifica a versão do Python usada no projeto (ex: com `pyenv`).      |
| `.github/workflows/`      | Workflows de CI/CD via GitHub Actions.                                 |
| `pyproject.toml`          | Configura metadados, dependências e ferramentas de build/lint.         |
| `requirements.txt`        | Lista de dependências do projeto para instalação com `pip`.            |
| `setup.cfg` (opcional)    | Configura ferramentas como `flake8`, `mypy`, `isort`.                  |
| `tox.ini` (opcional)      | Usado para testes em múltiplas versões do Python.                      |

# **Padrões de Código e Qualidade**
Manter padrões de codificação é essencial para garantir legibilidade, consistência e segurança. Abaixo, um conjunto de ferramentas recomendadas:

## Ferramentas por Categoria
| Categoria                | Ferramentas                      |
| ------------------------ | -------------------------------- |
| **Lint**                 | `flake8`, `pylint`, `prospector` |
| **Formatação**           | `black`, `blue`, `isort`         |
| **Verificação de Tipos** | `mypy`                           |
| **Docstrings**           | `pydocstyle`                     |
| **Segurança**            | `bandit`, `pip-audit`            |
| **Complexidade**         | `radon`                          |
| **Análise Geral**        | `SonarQube`, `prospector`        |

## Descrições das principais ferramentas
### `flake8`
* Valida estilo de código conforme a PEP 8.
* Integra com `pyflakes` e `mccabe` para detectar erros, más práticas e complexidade.

### `black`
* Formata automaticamente seu código conforme regras estritas e padronizadas.
* Filosofia: “sem configuração, sem discussão”.

### `mypy`
* Verifica se as **anotações de tipo** (type hints) estão sendo seguidas corretamente.

### `isort`
* Organiza os imports do Python automaticamente e em ordem alfabética.

### `pydocstyle`
* Valida se as docstrings seguem o padrão PEP 257.

### `bandit`
* Realiza análise estática de segurança no código Python, detectando vulnerabilidades comuns.

### `pip-audit`
* Analisa dependências instaladas para encontrar vulnerabilidades conhecidas com base em bancos como o NVD.

### `prospector`
* Ferramenta unificada que reúne outras como `mypy`, `pylint`, `pydocstyle` e `pep8`.

### `SonarQube`
* Plataforma completa de análise contínua de qualidade de código, cobertura de testes, bugs e vulnerabilidades.

### `radon`
* Mede a complexidade ciclomática e gera métricas de manutenibilidade do código.

# **Hooks com Pre-commit (Boa Prática)**
## Exemplo básico de `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.12.0
    hooks:
      - id: isort
```

## Como ativar:
```bash
pip install pre-commit
pre-commit install
```

# **Exemplo de Estrutura Final**
```bash
meu_projeto/
├── src/
│   └── app/
│       ├── main.py
│       ├── models/
│       ├── routers/
│       ├── services/
│       ├── core/
│       ├── utils/
│       └── __init__.py
├── tests/
│   └── test_alguma_funcionalidade.py
├── docs/
│   └── index.md
├── scripts/
│   └── setup_dev_env.sh
├── .gitignore
├── README.md
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
├── .python-version
└── .github/
    └── workflows/
        └── ci.yml
```