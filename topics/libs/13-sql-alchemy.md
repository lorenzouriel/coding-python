# SQL Alchemy
An ORM library is a common library written in the language of your choice that encapsulates the code needed to manipulate data, so you no longer use SQL

You **interact directly with an object in the same language you are using.**

SQL Alchemy is the most used ORM library!

### General Structure
![sql_alchemy_general_structure](/imgs/orm/sql_alchemy_general_structure.png)

- `Engine`: The Engine is the **starting point for any SQLAlchemy application.** It’s “home base” for the actual database and its DBAPI, **delivered to the SQLAlchemy application through a connection pool and a Dialect, which describes how to talk to a specific kind of database/DBAPI combination.**

- `Dialects`: The dialect is **the system SQLAlchemy uses to communicate with various types of DBAPI implementations and databases.** All dialects **require that an appropriate DBAPI driver is installed.** We can connect to some dialects like: PostgreSQL, MySQL and MariaDB, SQLite, Oracle, Microsoft SQL Server and more.

- `Pooling`: The **`Engine` will ask the connection pool for a connection when the `connect()` or `execute()` methods are called.** The default connection pool, `QueuePool`, **will open connections to the database on an as-needed basis.** 
    - As concurrent statements are executed, `QueuePool` will **grow its pool of connections to a default size of five, and will allow a default `“overflow”` of ten.** 
    - Since the Engine is essentially “home base” for the connection pool, it follows that you should keep a single Engine per database established within an application, rather than creating a new one for each connection.

- `DBAPI`: Is shorthand for the phrase `“Python Database API Specification”`. This is a widely **used specification within Python to define common usage patterns for all database connection packages.** The DBAPI is a “low level” API which is **typically the lowest level system used in a Python application to talk to a database.** 
    - SQLAlchemy’s dialect system is **constructed around the operation of the DBAPI, providing individual dialect classes which service a specific DBAPI on top of a specific database engine;** for example, the `create_engine()` URL `postgresql+psycopg2://@localhost/test` refers to the `psycopg2` DBAPI/dialect combination, whereas the URL `mysql+mysqldb://@localhost/test` refers to the MySQL for Python DBAPI/dialect combination.

- *[Check the doc here](https://docs.sqlalchemy.org/en/20/core/engines.html#pooling)*


## SQL Alchemy Guide

### Installation

You can install it using `pip`:
```python
pip install sqlalchemy
```

### Connecting to SQLite (Hello world!)

SQLite is a lightweight database that is great for learning the basics of SQLAlchemy. Here's a basic example of how to create a connection engine to an in-memory SQLite database:
```python
from sqlalchemy import create_engine

# Connect to SQLite in memory
engine = create_engine('sqlite:///mydatabase.db', echo=True)

print("Connection to SQLite established.")
```

### Creating our MAPPING
- `Object <---> Line`
- `Class <---> Table`
- `Attribute <---> Column` 

Before inserting or querying data, we need to define the models and create corresponding tables in the database:
```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)
```

### Creating Sessions and Inserting Data

Sessions in SQLAlchemy are used to maintain a 'workspace' for all the object operations you want to synchronize with the database:
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("User inserted successfully.")
```

### Querying Data

Now, let's query the data to verify the insertion:
```python
usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"User found: {usuario.nome}, Age: {usuario.idade}")
```

### Using Session `with` with Statement

When using with, you benefit from automatic entry and exit of contexts, meaning that at the end of the with block, **SQLAlchemy automatically closes the session or performs commit/rollback, depending on the operation's outcome.** This helps prevent connection leaks and ensures that transactions are properly managed.

**Advantages of Using with Statement with SQLAlchemy**

- **Automatic transaction management:** Transactions are automatically committed or rolled back depending on whether exceptions were raised within the block.

- **Automatic session closing:** This ensures that resources are released in a timely manner, avoiding connection leaks.

#### Example Without Using `with`

Without using the context manager, you need to manually manage the session, including commits, rollbacks, and session closure:
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
```
In this example, **all steps to ensure that the session is properly managed are explicit**: committing changes, handling exceptions, rolling back if something goes wrong, and finally closing the session.

#### Example Using `with`
When you use the context manager `with`, many of these steps are automated:
```python
from sqlalchemy.orm import sessionmaker, Session

Session = sessionmaker(bind=engine)

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    # Commit is automatically performed here if no exceptions occur
    # Rollback is automatically called if an exception occurs
    # Session is automatically closed upon exiting the with block
```

In the above example, SQLAlchemy handles commit, rollback, and session closure automatically. If an exception occurs within the with block, a rollback is called. When the with block completes without errors, the commit is performed, and in both cases, the session is automatically closed at the end.