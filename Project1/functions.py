FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of
    to-do items.
    """
    with open(filepath,"r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_args, filepath=FILEPATH):
    """ Writes the to-do items list in the text
    file.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_args)

if __name__ == "__main__":
    print(get_todos())