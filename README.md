# 🛍️ Product Management System

A simple **Product Management System** built with **Django**, allowing users to **sign up, log in, add, edit, delete, and search products** securely with authentication.

---

## 🚀 Features

- User Signup, Login, and Logout  
- Add New Products  
- Edit Existing Products  
- Delete Products  
- Search Products by Name  
- Fully Secured with Django’s Authentication System  

---

## 🧩 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (default)
- **Authentication:** Django built-in auth

---

## 📂 Project Structure

Product_Management_System/
│
├── inventory/
│ ├── migrations/
│ ├── templates/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── product_list.html
│ │ ├── form.html
│ │ └── delete_confirm.html
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── conf/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── db.sqlite3


---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SatyajitKumar123/Product_Management_System.git
cd Product_Management_System

```
### 2️⃣ Create a Virtual Environment
```

python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

```
### 3️⃣ Install Dependencies
```
pip install django

```
### 4️⃣ Run Migrations
```

python manage.py makemigrations
python manage.py migrate

```
### 5️⃣ Create a Superuser (optional)
```
python manage.py createsuperuser

```
### 6️⃣ Run the Server
```

python manage.py runserver
