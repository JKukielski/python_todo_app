prompt = "Enter todo: "
todos = []
while True:
    todo = input(prompt)
    todos.append(todo)
    print(todos)

#password checker
password = input("Enter password: ")
while password != "pass123":
    password = input("Enter password: ")

print("Password correct!")

#series of numbers
x = 1
while x <= 6:
    print(x)
    x = x + 1
