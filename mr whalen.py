users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David,"},
    {"name": "Eve", "role": "moderator"}
]

""" def admin():
    for i in range(len(users)):
        try:
            if [i][2] == "admin":
                print([i][1])
        except KeyError:
            continue
admin() """

for user in users:
    try:
        if user["role"] == "admin":
            print(user)
    except KeyError: 
        continue 