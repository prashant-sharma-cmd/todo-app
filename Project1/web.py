import functions
import streamlit as st

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to keep track of your activities.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")

