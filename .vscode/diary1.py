import streamlit as st
import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

# Hàm để thực hiện đăng ký tài khoản
def register(email, password):
    # Kiểm tra xem email đã tồn tại trong cơ sở dữ liệu chưa
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    if cursor.fetchone() is not None:
        return False
    
    # Thêm người dùng vào cơ sở dữ liệu
    cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password))
    conn.commit()
    return True

# Thiết lập trang
st.set_page_config(page_title="Đăng_ký", layout="centered")

# Tiêu đề
st.title("Đăng ký")

# Form đăng ký
with st.form("register_form"):
    email = st.text_input("Email")
    password = st.text_input("Mật khẩu", type="password")
    confirm_password = st.text_input("Xác nhận mật khẩu", type="password")
    submit_button = st.form_submit_button("Đăng ký")

    if submit_button:
        if email and password and confirm_password:
            if password != confirm_password:
                st.error("Mật khẩu không khớp. Vui lòng kiểm tra lại.")
            else:
                if register(email, password):
                    st.success("Đăng ký thành công!")
                else:
                    st.error("Email đã được sử dụng. Vui lòng chọn email khác.")
        else:
            st.warning("Vui lòng nhập đầy đủ thông tin.")

# Đóng kết nối đến cơ sở dữ liệu
conn.close()