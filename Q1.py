import streamlit as st
st.slider('Select a value:', 1, 10, 4)
stat =st.checkbox('labe', key=None, help=None, on_change=None, args=None, kwargs=None)
st.text(stat)