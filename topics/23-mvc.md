# MVC (Model View Controller)
MVC is a design pattern used to decouple the **user interface (View)**, **data (Model)**, and **application logic (Controller)**. This pattern helps achieve a separation of concerns.

Using the MVC pattern for websites, **requests are routed to a Controller that is responsible for working with the Model to perform actions and/or retrieve data.** The **Controller chooses the View to display and provides it with the Model.** View renders the final page, based on the data in the Model.

The rchitectural pattern separates an application into three main groups of components: **Models**, **Views**, and **Controllers**. 

**This pattern helps to achieve separation of concerns.** 

### Models
Create clean model classes and easily associate them with the database. Define validation rules declaratively, using attributes, which are applied on the client and server.

**Represents the data and business logic of the application.** Typically, the **model consists of classes that handle data storage, manipulation, and validation.** It doesn't know anything about how the data will be presented to the user.

### View
**Is the presentation layer of the application.** It **displays the data from the model to the user in a way that is understandable and interactive.** Views are usually created using HTML, CSS, and other **frontend technologies.**


### Controllers
Simply **route requests to controller actions, implemented as normal methods.** The request path, query string, and request body data are automatically associated with the method parameters.

Is **responsible for receiving user requests, interacting with the model to perform necessary operations, and selecting the appropriate view to display the results.** The controller **acts as an intermediary between the view and the model, controlling the flow of the application.**

## Example with Python

1. **Model (`model.py`):** Defines the data and business logic.
```python
class TodoItem:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, title):
        new_id = len(self.todos) + 1
        todo = TodoItem(new_id, title)
        self.todos.append(todo)

    def get_all_todos(self):
        return self.todos
```


2. **View (`templates/index.html`):** Defines the presentation layer using HTML.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    <h1>Todo List</h1>
    <ul>
        {% for todo in todos %}
            <li>{{ todo.title }}</li>
        {% endfor %}
    </ul>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Enter a new todo">
        <button type="submit">Add Todo</button>
    </form>
</body>
</html>
```

3. **Controller (`app.py`):** Handles user requests, interacts with the model, and selects the appropriate view to display.
```python
from flask import Flask, render_template, request, redirect
from model import TodoList

app = Flask(__name__)
todo_list = TodoList()

@app.route('/')
def index():
    todos = todo_list.get_all_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    todo_list.add_todo(title)
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
```

### In this example:

- The `model.py` file **defines the TodoItem and TodoList classes, representing individual todo items and a list of todo items, respectively.**
- The `templates/index.html` file **contains the HTML code to display the todo list and a form to add new todo items.**
- The `app.py` file is the **main application file.** It **uses Flask to handle routing and request handling.** 
- The `index` **route renders the HTML template with the todo list, and the add_todo route handles adding new todo items to the list.**
































































































