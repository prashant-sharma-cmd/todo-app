import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to keep track of your activities.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state["new_todo"]
        st.rerun()

st.text_input(label="Add Todo",
              label_visibility="collapsed",
              placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

