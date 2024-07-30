create database diary_app;
use diary_app;
CREATE TABLE Categories (
    categories_id NUMBER PRIMARY KEY,
    name VARCHAR2(255),
    id NUMBER
);

CREATE TABLE "User" (
    user_id NUMBER PRIMARY KEY,
    name VARCHAR2(255),
    age NUMBER,
    password_hash VARCHAR2(255),
    mail VARCHAR2(255),
    full_name VARCHAR2(255),
    date_of_birth DATE,
    created_at TIMESTAMP,
    last_login TIMESTAMP,
    login_count NUMBER,
    updated_at TIMESTAMP,
    is_active VARCHAR2(1), -- Oracle does not have BOOLEAN type, use CHAR(1) for boolean flags
    role VARCHAR2(50)
);

CREATE TABLE Entries (
    entry_id NUMBER PRIMARY KEY,
    user_id NUMBER,
    title VARCHAR2(255),
    content_hash VARCHAR2(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    is_public VARCHAR2(1), -- Use CHAR(1) for boolean flags
    categories_id NUMBER,
    tags VARCHAR2(255),
    FOREIGN KEY (user_id) REFERENCES "User"(user_id),
    FOREIGN KEY (categories_id) REFERENCES Categories(categories_id)
);

CREATE TABLE Login_History (
    login_id NUMBER PRIMARY KEY,
    user_id NUMBER,
    login_time TIMESTAMP,
    ip_address VARCHAR2(255),
    device_info VARCHAR2(255),
    logout_time TIMESTAMP,
    login_status VARCHAR2(50),
    FOREIGN KEY (user_id) REFERENCES "User"(user_id)
);

-- Optionally, you may want to create sequences for auto-incrementing primary keys
-- Example for User table:
CREATE SEQUENCE User_seq START WITH 1 INCREMENT BY 1;

-- Example of how to use the sequence to insert data into the User table:
-- INSERT INTO User (user_id, name, age, password_hash, mail, full_name, date_of_birth, created_at, last_login, login_count, updated_at, is_active, role)
-- VALUES (User_seq.NEXTVAL, 'John Doe', 30, 'hashedpassword', 'john@exa
