import streamlit as st
import requests

# Hàm để thực hiện đăng nhập


def login(email, password):
    # Gửi request đến API đăng nhập của bạn
    response = requests.post(
        "http://localhost:8000/token",
        data={"username": email, "password": password}
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    return None


# Thiết lập trang
st.set_page_config(page_title="Đăng_nhập", layout="centered")

# Tiêu đề
st.title("Đăng nhập")

# Form đăng nhập
with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")
    submit_button = st.form_submit_button("Đăng nhập")

    if submit_button:
        if email and password:
            token = login(email, password)
            if token:
                st.success("Đăng nhập thành công!")
                st.session_state['token'] = token
                st.experimental_rerun()
            else:
                st.error(
                    "Đăng nhập thất bại. Vui lòng kiểm tra lại email và mật khẩu.")
        else:
            st.warning("Vui lòng nhập email và mật khẩu.")

# Kiểm tra xem người dùng đã đăng nhập chưa
if 'token' in st.session_state:
    st.write(
        f"Bạn đã đăng nhập. Token của bạn là: {st.session_state['token']}")
    if st.button("Đăng xuất"):
        del st.session_state['token']
        st.experimental_rerun()
