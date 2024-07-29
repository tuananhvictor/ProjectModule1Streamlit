# Diary App

**Diary App** là một ứng dụng quản lý nhật ký được xây dựng bằng FastAPI và SQLAlchemy. Ứng dụng cho phép người dùng tạo và quản lý các mục nhật ký, danh mục và lịch sử đăng nhập.

## Mục Lục

- [Giới Thiệu](#giới-thiệu)
- [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
- [Cài Đặt](#cài-đặt)
- [Cấu Hình](#cấu-hình)
- [Chạy Ứng Dụng](#chạy-ứng-dụng)
- [Tạo Cơ Sở Dữ Liệu](#tạo-cơ-sở-dữ-liệu)
- [API Endpoints](#api-endpoints)
- [Tài Liệu](#tài-liệu)
- [Giấy Phép](#giấy-phép)

## Giới Thiệu

**Diary App** là một ứng dụng web cho phép người dùng quản lý các mục nhật ký của mình. Ứng dụng sử dụng FastAPI cho backend và SQLAlchemy cho ORM. 

## Tình Hình Hiện Tại

    Project của tụi em liên quan tới chủ để bảo mật thông tin. Nên tụi em sẽ xây dựng 1 app có chức năng bảo mật các thông tin như tên, password, nhật kí,..
    
    Hiện app chạy trên web bằng thư viện Streamlit của Python. Đã sơ bộ xây dựng xong function đăng kí và đăng nhập tài khoản. Thông tin đăng kí/đăng nhập sẽ được mã hóa (Caesar Cipher) rồi sẽ được chuyện thẳng dự trữ trong database

    Chưa xây dựng xong function viết nhật kí, cũng được mã hóa và dự trữ tương tự. Và khi user muốn coi lại thì sẽ convert mã ngược lại thành text

    Group đang tìm hiểu thêm các cách để bảo vệ bộ mã đó ( vì sẽ có tool giải được nếu xâm nhập vô được). Có ý tưởng là sẽ chèn các kí tự ngẫu hiên vào bộ mã mà chỉ có hệ thống biết, và sẽ tự loại bỏ khi convert cho user ( làm khó các tool giải). Tuy vậy vẫn chưa tìm được phương án nào để thực thi việc đó.

### Các Tính Năng Chính

- Tạo và quản lý người dùng
- Thêm và chỉnh sửa các mục nhật ký
- Quản lý danh mục của các mục nhật ký
- Theo dõi lịch sử đăng nhập

## Yêu Cầu Hệ Thống

- Python 3.8 trở lên
- MySQL 5.7 trở lên (hoặc MariaDB tương thích)
- Các thư viện Python (được liệt kê trong `requirements.txt`)

## Cấu Trúc Hệ Thống
    
    app/
    │
    ├── backend/
    │ ├── init.py
    │ ├── main.py
    │ ├── config.py
    │ ├── database.py
    │ ├── models.py
    │ ├── schemas.py
    │ ├── initialization.py
    │ └── utils.py
    │
    ├── frontend/
    │ ├── init.py
    │ └── app.py
    │
    ├── .env.txt
    └── requirements.txt


## Mô Tả Database

    https://lucid.app/lucidchart/2c3b4c86-7de7-431d-802a-d05de35eea9d/edit?viewport_loc=-1918%2C-1574%2C3072%2C1482%2C0_0&invitationId=inv_75bc71bb-1662-4470-abb4-e9d3ebe3f33d
    
## Cài Đặt

1. **Clone Dự Án**

   ```sh
   git clone https://github.com/tuananhvictor/ProjectModule1Streamlit/tree/main/.vscode/my_project
   cd your-repository/my_project


2. Tạo Môi Trường Ảo: Tạo môi trường ảo để quản lý các phụ thuộc.

    python -m venv venv

3. Kích Hoạt Môi Trường Ảo:

    +Trên macOS/Linux:
        source venv/bin/activate
    +Trên window:
        venv\Scripts\activate

4. Cài Đặt Các Phụ Thuộc: Cài đặt các thư viện cần thiết

    pip install -r requirements.txt



    



## Cấu Hình

1. Tạo Tệp .env: Tạo tệp .env trong thư mục gốc của dự án và cấu hình các biến môi trường sau:

    DB_USER=root
    DB_PASS=password
    DB_HOST=localhost
    DB_PORT=port_id
    DB_NAME=database_name

## Chạy ứng dụng
    
1. Khởi Động Dự Án: Chạy ứng dụng bằng Uvicorn

    uvicorn backend.main:app --reload

    Ứng dụng sẽ chạy tại http://127.0.0.1:8000.

2. **Khởi Tạo Cơ Sở Dữ Liệu**:
   - Chạy script `initialization.py` để tạo các bảng trong cơ sở dữ liệu.
     ```sh
     python -m backend.initialization
     ```

3. **Chạy Ứng Dụng**:
   - Khởi động ứng dụng backend bằng Uvicorn.
     ```sh
     uvicorn backend.main:app --reload
     ```
   - Truy cập ứng dụng tại `http://127.0.0.1:8000`.

4. **Phát Triển Giao Diện Người Dùng**:
   - Nếu cần, chạy ứng dụng frontend từ `app/frontend/app.py` bằng công cụ tương ứng (ví dụ: Streamlit).

## API Endpoint

1. Tạo người dùng 

    URL: /users
    Phương Thức: POST
    Thân Yêu Cầu:
        {
    "name": "John Doe",
    "mail": "john.doe@example.com",
    "full_name": "Johnathan Doe",
    "age": 30,
    "date_of_birth": "1994-06-15",
    "password": "yourpassword"
    }

    Thân Phản Hồi:
                {
    "user_id": 1,
    "name": "John Doe",
    "mail": "john.doe@example.com",
    "full_name": "Johnathan Doe",
    "age": 30,
    "date_of_birth": "1994-06-15",
    "created_at": "2024-07-29T00:00:00",
    "last_login": null,
    "login_count": 0,
    "updated_at": null,
    "is_active": true,
    "role": "user"
    }

## Danh Sách Các API Khác

    /entries - Thêm và quản lý các mục nhật ký.
    /categories - Quản lý các danh mục.
    /login-history - Theo dõi lịch sử đăng nhập.

## Tài Liệu

    FastAPI Documentation
    SQLAlchemy Documentation
    Python-dotenv Documentation





