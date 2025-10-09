import streamlit as st
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def toggle_message():
    st.session_state.clicked = not st.session_state.clicked

st.button("Click me!", on_click=toggle_message)

if st.session_state.clicked:
    st.write("Hello!")
else:
    st.write("Buy!")