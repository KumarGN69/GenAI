import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)