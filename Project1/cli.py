# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    action = input("Type add, show, edit, complete or exit: ")
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]
        todos = functions.get_todos("todos.txt")

        todos.append(todo+'\n')

        functions.write_todos(todos)

    elif action.startswith('show'):
        todos = functions.get_todos("todos.txt")

        # new_todos = [item.strip('\n') for item in todos]

        for index,task in enumerate(todos):
            output = f"{index + 1}-{task.strip('\n')}"
            print(output)

    elif action.startswith('edit'):
        try:
            todos = functions.get_todos("todos.txt")

            number = int(action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith('exit'):
        break

    elif action.startswith('complete'):
        try:
            todos = functions.get_todos("todos.txt")

            index = int(action[9:]) - 1
            todo_to_remove = todos[index].strip('\n')
            todos[index] = todo_to_remove
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo: {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    else:
        print("Invalid input!! Please try again.")

print("Bye!")

