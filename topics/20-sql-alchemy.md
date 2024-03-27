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

---



