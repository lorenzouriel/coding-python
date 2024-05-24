# SQLModel 
Is a library for **interacting with SQL databases from Python code, with Python objects.** It is designed to be intuitive, easy to use, highly compatible, and robust.

SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.

**The key features are:**
- **Intuitive to write:** Great editor support. Completion everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
- **Easy to use:** It has sensible defaults and does a lot of work underneath to simplify the code you write.
- **Compatible:** It is designed to be compatible with FastAPI, Pydantic, and SQLAlchemy.
- **Extensible:** You have all the power of SQLAlchemy and Pydantic underneath.
- **Short:** Minimize code duplication. A single type annotation does a lot of work. No need to duplicate models in SQLAlchemy and Pydantic.

**Code Example:**
```python
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()
```

**Code Breakdown:**
- **Imports:** This line imports the `Optional` class from the typing module. Optional is used to indicate that a variable can be of a specific type or None.
```python
from typing import Optional
```

- **Imports:** This line imports necessary classes and functions from the `sqlmodel` module.
    - `Field`: Used to define fields in the database table.
    - `Session`: Represents a session for database operations.
    - `SQLModel`: Base class for declarative class definitions.
    - `create_engine`: Function used to create a connection to the database.
```python
from sqlmodel import Field, Session, SQLModel, create_engine
```

- **Class Definition:**
    - `Hero`: This class inherits from SQLModel and is defined with table=True, **indicating that it represents a database table.**
    - Attributes `id`, `name`, `secret_name`, and `age` are defined as class variables.
    - `id`: An optional integer field representing the primary key of the table. It's marked as optional (`Optional[int]`) and has a default value of `None`. It's also specified as the primary key of the table.
    - `name` and `secret_name`: Required string fields representing the hero's name and secret name, respectively.
    - `age`: An optional integer field representing the hero's age. It defaults to `None`.
```python
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
```

- **Database Engine Creation:** This line creates an **SQLite database engine** that connects to the `database.db` file. The `echo=True` argument enables logging of SQL commands.
```python
engine = create_engine("sqlite:///database.db", echo=True)
```

- **Table Creation:** This line **creates the database table corresponding to the Hero class using the SQLModel metadata** and the database engine created earlier.
```python
SQLModel.metadata.create_all(engine)
```

- **Object Creation:** Two `Hero` objects (`hero_1` and `hero_2`) are created with different attributes (`name`, `secret name`, and `age`).
```python
hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
```

- **Database Interaction:** A session is **created using the database engine.** The `hero_1` and `hero_2` objects are added to the session, and the `changes are committed to the database.` The `with statement` ensures that the **session is properly closed after the block is executed, handling exceptions and resource cleanup automatically.**
```python
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()
```

- *[You can check the docs here](https://sqlmodel.tiangolo.com/)*