import streamlit as st
import requests

API_URL = "http://localhost:8000"

def login(username, password):
    response = requests.post(f"{API_URL}/token", data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def register(username, email, password, full_name):
    response = requests.post(
        f"{API_URL}/users",
        json={"name": username, "mail": email, "password": password, "full_name": full_name}
    )
    return response.status_code == 200

st.set_page_config(page_title="User Authentication", layout="centered")

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if username and password:
                token = login(username, password)
                if token:
                    st.success("Login successful!")
                    st.session_state['token'] = token
                    st.experimental_rerun()
                else:
                    st.error("Login failed. Please check your credentials.")
            else:
                st.warning("Please enter both username and password.")

with tab2:
    st.header("Register")
    with st.form("register_form"):
        new_username = st.text_input("Username")
        new_email = st.text_input("Email")
        new_full_name = st.text_input("Full Name")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button("Register")

        if submit_button:
            if new_username and new_email and new_full_name and new_password and confirm_password:
                if new_password == confirm_password:
                    if register(new_username, new_email, new_password, new_full_name):
                        st.success("Registration successful! Please login.")
                    else:
                        st.error("Registration failed. Please try again.")
                else:
                    st.error("Passwords do not match.")
            else:
                st.warning("Please fill in all fields.")

if 'token' in st.session_state:
    st.write(f"You are logged in. Your token is: {st.session_state['token']}")
    if st.button("Logout"):
        del st.session_state['token']
        st.experimental_rerun()
