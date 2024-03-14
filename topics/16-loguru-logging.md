# Loguru and Logging
Loguru is a logging library for Python that aims to bring a simpler and more powerful user experience than Python's standard logging module. 

With a simple API, Loguru offers several useful features, such as file rotation, JSON serialization, sending messages to multiple destinations, and much more, all without the need for complicated initial configuration.

### Whats is Logging?
Logging is the process of recording messages that document events that occur during the execution of software. 

These messages may indicate execution progress, failures, errors, or other useful information. 

Logging is crucial for software development and maintenance, as it allows developers and system administrators to understand what the application is doing, diagnose problems, and monitor performance in production.

### How to use Loguru?
To start using Loguru, you first need to install it. This can be done easily via pip:
`poetry add loguru`

### Examples:

- **1 - Basic Logging**
```python
from loguru import logger

# Log messages of different levels
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")

# The output will be displayed in the console
``` 
*In this example, we use the `logger` imported from `Loguru` to record messages of different severity levels. Loguru takes care of formatting and displaying these messages in the console, by default.*


- **2 - File Log Config**

Here we configure Loguru to save log messages to a file, including file rotation based on size.
```python
from loguru import logger

# Config log file with 5mb
logger.add("meu_app.log", rotation="5 MB")

logger.info("This message will be saved")
```

- **3 - Capturing Logging Excpetions**
```python
from loguru import logger

def minha_funcao():
    raise ValueError("Um erro aconteceu!")

try:
    minha_funcao()
except Exception:
    logger.exception("Uma exceção foi capturada")
```

Using `logger.exception()`, Loguru automatically captures and logs the exception traceback, which is extremely useful for error diagnosis.

- **4 - Capturing and Saving Logs**

Here is an example of how to configure loguru to save logs both to a file and display them to standard output (`stderr`):
```python
from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")
```

In this code, two `"sinks"` are added to the logger:
- `stderr`, to display the logs, with specific formatting that includes time, log level, message, and source file.
- `"my_logs_file.log"`, to save the logs to a file with a format that also includes time, level, message, and source file.

### How to use
Selecting the appropriate log level for different messages allows developers and system administrators to configure logs to capture only the information they need. 

For example, in a **development environment**, you may want to view all logs, from **DEBUG** to **CRITICAL**, to fully understand the application's behavior. In contrast, in a **production environment**, you can configure it to log only **WARNING**, **ERROR**, and **CRITICAL**, to reduce the volume of data generated and focus on issues that need attention.

- **Example of capturing exceptions:**
```python
from loguru import logger

def my_function():
    raise ValueError("An error!")

try:
    my_function()
except Exception:
    logger.exception("An exception was captured!")
```

Using `logger.exception()`, Loguru **automatically captures and logs the exception traceback, which is extremely useful for error diagnosis.**