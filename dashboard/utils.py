import streamlit as st

def page_header(title, subtitle=None):
    st.title(title)

    if subtitle:
        st.caption(subtitle)


def success_message(message):
    st.success(message)


def error_message(message):
    st.error(message)