# What is FastAPI?
FastAPI is a high-performance web framework for building APIs with Python 3.6+ based on declarative data types (thanks to Pydantic) and the ASGI (Asynchronous Server Gateway Interface) standard. It is designed to be easy to use, quick to learn, and highly efficient in terms of performance, offering native support for Python data types, data typing, automatic input validation, and automatic interactive documentation (generated automatically by Swagger UI and ReDoc).

### Key features:

Fast: Utilizes asynchronous Python and optimization techniques for high performance.
Easy to use: Has a declarative and intuitive syntax, allowing for rapid prototyping.
Data typing: Utilizes Python data typing to ensure data safety and consistency.
Automatic documentation: Automatically generates interactive documentation for your API.
OpenAPI and Swagger support: Full compatibility with these standards, allowing integration with other tools.
FastAPI usage examples:

### Creating a basic API:

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

#### Defining data models with Pydantic:

```python
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

### Challenge: [Create our first CRUD](/exercises/class19_fastapi/)

**1.  `POST /items/`: Creates a new item**

This route allows creating a new item in the database. **The client sends the data of the new item in the body of the HTTP request, and the server adds this item to the database.** Here's how it works:
- **HTTP Verb:** `POST`
- **Endpoint:** `/items/`
- **Action:** Creates a new item in the database.
- **Requirements:** The request body must contain the data of the new item.
- **Response:** Returns the newly created item.

**2. `GET /items/`: Returns a paginated list of items**

This route allows retrieving a paginated list of items from the database. **The client can optionally specify the skip (how many items to skip) and limit (how many items to return) parameters for pagination.** Here's how it works:

- **HTTP Verb:** `GET`
- **Endpoint:** `/items/`
- **Action:** Returns a paginated list of items from the database.
- **Query Parameters:** `skip` (optional, default = 0) and `limit` (optional, default = 10).
- **Response:** Returns a list of items as specified by the query parameters.

**3. `GET /items/{item_id}`: Returns a specific item based on ID**

This route allows **retrieving a specific item from the database based on the provided ID.** Here's how it works:

- **HTTP Verb:** `GET`
- **Endpoint:** `/items/{item_id}`
- **Action:** Returns a specific item based on the provided ID.
- **Path Parameters:** `item_id` (ID of the item to be retrieved).
- **Response:** Returns the item corresponding to the provided ID.

**4. `PUT /items/{item_id}`: Updates an existing item based on ID**

This route allows **updating the data of an existing item in the database based on the provided ID.** The client sends the new data of the item in the body of the HTTP request. Here's how it works:

- **HTTP Verb:** `PUT`
- **Endpoint:** `/items/{item_id}`
- **Action:** Updates an existing item based on the provided ID.
- **Path Parameters:** `item_id` (ID of the item to be updated).
- **Requirements:** The request body must contain the new data of the item.
- **Response:** Returns the updated item.

**5. `DELETE /items/{item_id}`**: Deletes an existing item based on ID

This route allows **deleting an existing item in the database based on the provided ID.** Here's how it works:

- **HTTP Verb:** `DELETE`
- **Endpoint:** `/items/{item_id}`
- **Action:** Deletes an existing item based on the provided ID.
- **Path Parameters:** `item_id` (ID of the item to be deleted).
- **Response:** Returns the deleted item.

**These operations provide a complete API for managing items in the database, allowing for efficient and secure creation, retrieval, updating, and deletion of items.** Ensure that the operations align with the requirements of your project and that you implement the necessary logic to ensure data consistency and security.