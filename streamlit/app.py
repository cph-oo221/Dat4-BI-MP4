import streamlit as st
import pandas as pd
from recommendation import get_recommendations

st.set_page_config(
    page_title="MP5",
    page_icon=":book:",
    layout="wide",
)

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

    if user_input == "Type Here ...":
        st.write("Please enter a valid input")
    else:
        recommendations = get_recommendations(user_input)
        if recommendations is None:
            st.write("No articles found")
        else:
            st.write(recommendations)
