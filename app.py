import streamlit as st

st.title("Medical Query Analyzer")

query = st.text_input(

    "Enter Medical Query"
)

if st.button("Analyze"):

    st.write(

        "Medical Answer Appears Here"
    )