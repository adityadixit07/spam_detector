# Django Spam Identifier API

## Overview
This project provides a REST API for identifying spam phone numbers and performing reverse lookups by phone number or name. It is built using Django with a MySQL backend, ensuring security and scalability.

---

## Features
- **User Registration and Login**: Secure user registration and JWT-based authentication.
- **Spam Reporting**: Mark phone numbers as spam for global identification.
- **Search**:
  - Search by name: Displays details and spam likelihood.
  - Search by phone number: Returns all associated names and spam likelihood.
- **User Profiles**: View details of registered users.
- **Database Population**: Populate the database with random sample data for testing.

---

## Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package installer)
- MySQL Client library

---

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up `.env` File
Create a `.env` file in the root directory and add the following:
```env
SECRET_KEY=your_secret_key_here
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

### 3. Set Up MySQL Database
1. Log in to MySQL:
   ```bash
   mysql -u root -p
   ```
2. Run the following SQL commands:
   ```sql
   CREATE DATABASE your_database_name;
   CREATE USER 'your_database_user'@'localhost' IDENTIFIED BY 'your_database_password';
   GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_database_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate Database (Optional)
Run the following script to populate the database with sample data:
```bash
python manage.py shell
>>> from utils.populate_db import populate_db
>>> populate_db()
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

---

## API Endpoints

### Public Endpoints
- **Register**: `POST /api/register/`
  - Request: `{ "username": "", "phone_number": "", "password": "" }`
- **Login**: `POST /api/login/`
  - Request: `{ "phone_number": "", "password": "" }`

### Protected Endpoints (JWT Required)
- **Mark Spam**: `POST /api/spam/`
  - Request: `{ "phone_number": "" }`
- **Search by Name**: `GET /api/search/?query=<name>`
- **Search by Phone Number**: `GET /api/search/?query=<phone_number>`
- **User Profile**: `GET /api/profile/`

---

## File Structure
```
project_root/
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
├── utils/
│   └── populate_db.py
├── project/
│   ├── settings.py
│   ├── urls.py
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── contacts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
└── db.sqlite3
```

## Notes
- Replace `your_secret_key_here` and database credentials with secure values.
- Always keep the `.env` file out of version control.
- This project is configured for local development; additional configurations are needed for production.

---
