## Nomenclaturas segundo a PEP 8 (Guia de Estilo do Python)

### 1. Variáveis, funções e atributos
* Formato: **snake_case** (letras minúsculas com underlines)
* Exemplo:
  ```python
  def calcular_media():
      nota_final = 7.5
  ```

### 2. Classes
* Formato: **CamelCase** (primeira letra de cada palavra em maiúscula, sem underlines)
* Exemplo:
  ```python
  class CalculadoraFinanceira:
      pass
  ```

### 3. Constantes
* Formato: **SCREAMING_SNAKE_CASE**
* Exemplo:
  ```python
  PI = 3.1415
  LIMITE_MAXIMO = 1000
  ```

### 4. Módulos e pacotes
* **Módulos**: nome do arquivo `.py` em **snake_case**
* **Pacotes**: diretórios também em **snake_case**
* Exemplo:
  ```
  meu_modulo.py
  pacote_utilidades/
  ```

### 5. Métodos e atributos "privados"
* Prefixo com um underscore (`_`)
* Indica uso interno (não é privado de fato, mas uma convenção)
* Exemplo:
  ```python
  class Pessoa:
      def _calcular_idade(self):
          pass
  ```

### 6. Métodos especiais
* Prefixo e sufixo com dois underlines (`__dunder__`)
* São métodos definidos pelo interpretador Python
* Exemplo:
  ```python
  def __init__(self):
      pass
  ```

### 7. Atributos com name mangling (ocultação)
* Prefixo com dois underlines, sem sufixo: `__nome`
* Gera modificação interna de nome para evitar colisões em subclasses
* Exemplo:
  ```python
  class Exemplo:
      def __interno(self):
          pass
  ```

## Convenções a evitar
| Nome          | Motivo                                                    |
| ------------- | --------------------------------------------------------- |
| `l`, `O`, `I` | Letras isoladas confundem com números (1 e 0)             |
| `__nome__`    | Reservado para métodos especiais definidos pela linguagem |
| `nome__`      | Pode entrar em conflito com futuras palavras-chave        |
