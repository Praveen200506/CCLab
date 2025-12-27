import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("FastAPI + Streamlit Web App")

if st.button("Home"):
    res = requests.get(f"{API_URL}/")
    st.json(res.json())

if st.button("Hello"):
    res = requests.get(f"{API_URL}/hello")
    st.json(res.json())

st.divider()

st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        payload = {
            "username": username,
            "password": password
        }
        res = requests.post(f"{API_URL}/login", json=payload)
        st.json(res.json())
    else:
        st.warning("Please enter username and password")
