# Django-Role-Based-Authentication-API
Here’s a complete `README.md` for your **Django Role-Based Authentication API** project. This assumes you're using `SimpleJWT`, Django REST Framework, and a custom user model with role handling:

---

```markdown
# 🛡️ Django Role-Based Authentication API

This project implements **Role-Based Authentication** using **Django**, **Django REST Framework**, and **JWT (JSON Web Tokens)** with **SimpleJWT**.

---

## ✅ Features

- User registration with role assignment (`admin`, `user`, `seller`, etc.)
- JWT-based login and token authentication
- Permissions based on user roles
- API-ready for frontend integration (React, Vue, etc.)
- CORS enabled for cross-origin requests

---

## 🏗️ Project Structure

```

ecommerce/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── ecommerce/
│   └── settings.py
├── manage.py

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/django-role-auth-api.git
cd django-role-auth-api
````

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Apply migrations and run server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🧑‍💻 API Endpoints

### 🔐 Registration

**POST** `/api/register/`

```json
{
  "username": "john",
  "password": "mypassword123",
  "role": "user"
}
```

### 🔑 Login

**POST** `/api/login/`

```json
{
  "username": "john",
  "password": "mypassword123"
}
```

**Response:**

```json
{
  "access_token": "<jwt_token>",
  "refresh_token": "<refresh_token>"
}
```

### 🔒 Protected Route (Authenticated)

**GET** `/api/protected/` (Example)

Use JWT Bearer token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

---

## 🧠 Custom User Model

```python
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    SELLER = 'seller'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User'),
        (SELLER, 'Seller'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)
```

---

## 🛠️ Permissions Example

```python
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'
```

Use it in views:

```python
permission_classes = [IsAdminUser]
```

---

## ⚙️ JWT Configuration

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

---

## 🌐 CORS Setup

```python
# settings.py
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOW_ALL_ORIGINS = True
```

---

## 📦 Requirements

```txt
Django>=5.0
djangorestframework
djangorestframework-simplejwt
django-cors-headers
```

---

## 🧾 License

This project is licensed under the MIT License.

---

## 📡 Deployment Tip

To deploy on production, make sure to:

* Set `DEBUG = False`
* Set allowed hosts
* Use secure keys
* Use HTTPS (via Nginx + Gunicorn or other)

---

## 📤 Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit with role-based auth"
git remote add origin https://github.com/<your-username>/django-role-auth-api.git
git push -u origin master
```

---

## 👋 Author

Made with ❤️ by [Mustakim](shaikhmustakim2942@gmail.com)

```

---

Would you like me to generate this `README.md` file and save it into your project structure as well?
```
