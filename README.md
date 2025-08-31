# 📌 Subscription Management App

A backend application built with **Django REST Framework** that helps users manage and track their recurring subscriptions (e.g., Netflix, Spotify, SaaS tools). The app provides APIs for authentication, subscription CRUD operations, dashboards, and reminders.

---

## 🚀 Features

- **User Authentication** (Token-based)
- **Subscription Management** (Add, Update, Delete, List)
- **Billing Tracking** (Amount, Frequency, Due Dates)
- **Tags/Categories** (Entertainment, Utilities, Productivity, etc.)
- **Dashboard** (Monthly/Yearly cost overview)
- **Notifications** (Email reminders for upcoming billing)
- **Search & Filter** subscriptions
- **Pagination** subscriptions

---

## 🏗️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** Token Auth (`djangorestframework-authtoken`)
- **Database:** PostgreSQL (or SQLite for local dev)
- **Deployment:** Render

---

## 📂 Project Structure

```
subscription-management-django-app/
│── manage.py
│── requirements.txt
│── README.md
│── .env
│── .gitignore
│── media
│   ├── profiles              # storage location for user profile photo
│── subscription_app/         # main project settings
│── subscriptions/            # app for subscription features
│   ├── models.py             # Subscription model
│   ├── views.py              # API views
│   ├── serializers.py        # DRF serializers
|   ├── admin.py              # admin panel config
│   ├── urls.py               # API routes
|   ├── filters.py            # Custom filtering
|   ├── permissions.py        # Custom permissions
│── account/                  # app for authentication
    ├── models.py             # Custom user model
    ├── views.py              # account API views
    ├── serializers.py        # DRF serializers
    ├── urls.py               # account routes
    ├── signals.py            # signals for automatic token and profile creation
    ├── admin.py              # admin panel config
    ├── apps.py

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sonofbossman/Subscription-Management-Django-App.git
cd subscription-management-django-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file in the root folder (copy from `.env.example`):

```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_host_environment
DB_PORT=your_db_port
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

| Endpoint                   | Method | Description                        |
| -------------------------- | ------ | ---------------------------------- |
| `/api/`                    | GET    | API Root                           |
| `/api/auth/register/`      | POST   | Register a new user                |
| `/api/auth/login/`         | POST   | User login (Token)                 |
| `/api/auth/logout/`        | POST   | User logout (IsAuthenticated)      |
| `/api/auth/profile/`       | GET    | View own profile (IsAuthenticated) |
| `/api/auth/profile/`       | PATCH  | Edit own profile (IsAuthenticated) |
| `/api/subscriptions/`      | GET    | List all user subscriptions        |
| `/api/subscriptions/`      | POST   | Create a new subscription          |
| `/api/subscriptions/<id>/` | GET    | Retrieve subscription details      |
| `/api/subscriptions/<id>/` | PUT    | Update a subscription              |
| `/api/subscriptions/<id>/` | DELETE | Delete a subscription              |
| `/api/dashboard/`          | GET    | Subscription summary & insights    |

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📖 API Documentation

Interactive API docs available at:

- browsable APi → `/https://sma-976s.onrender.com//`

---

## 🚀 Deployment

The app is deployed on:

- **Render**

Make sure to:

- Configure production `.env` values
- Set `DEBUG=False`
- Run `collectstatic` if needed

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a PR.

---

## 📜 License

This project is yet to be licensed.

---
