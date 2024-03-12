users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": ""},
    {"name": "Carol", "email": "carol@example.com"}
]

valid_users = [user for user in users if user["email"]]

print(valid_users)