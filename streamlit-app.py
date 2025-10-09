import streamlit as st
st.header('st.button')
clicked = st.button("Click me!")
if clicked:
    st.write('Hellow there!')
else:
    st.write('Goodbye')