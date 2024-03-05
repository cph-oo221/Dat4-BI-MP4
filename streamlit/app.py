import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MP5",
    page_icon=":book:",
    layout="wide",
)

df = pd.read_csv("../data/HR-Employee-Attrition.csv")

st.markdown(
    """
    ### Finding text pieces/articles related to user input: 
    <style>
        .stButton>button:focus:not(:active) {
            border: none !important;
        }
        .stButton>button:hover {
            border-color: green !important;
        }
        .stButton>button {
            color : white !important;
        }
    </style>
    """
, unsafe_allow_html=True)


user_input = st.text_input("User input", "Type Here ...")


if st.button("Submit"):
    st.write(user_input)
