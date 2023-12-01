import streamlit as st
import functions

st.title("To Do App")

st.subheader("This is my To Do App")
st.write("This App helps to increase your Productivity")

todos = functions.get_todo()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter To Do", placeholder="Add new to do here...")

