# 📊  Accounting & Ledger Management System

A fully functional Accounting & Ledger Management System built using **Django** with customized **Django Admin**, dynamic ledger calculations, and PDF export functionality.

This project demonstrates financial logic implementation, admin customization, and backend architecture design.

---

## ✨ Features

* 👤 Party Management (Customers / Vendors)
* 💳 Debit & Credit Transaction Recording
* 📒 Automatic Ledger Generation
* 📆 Date-wise Ledger Filtering
* 📊 Opening & Running Balance Calculation
* 🧮 Monthly Transaction Summary
* 📄 PDF Ledger Export (ReportLab)
* 🔐 Django Admin Custom Interface
* ⚡ Optimized ORM Queries using Aggregations

---

## 🛠 Tech Stack

| Technology          | Purpose          |
| ------------------- | ---------------- |
| Python              | Core Programming |
| Django              | Web Framework    |
| SQLite / PostgreSQL | Database         |
| ReportLab           | PDF Generation   |
| Django Admin        | UI & Management  |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/django-accounting-app.git
cd django-accounting-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Access Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## 🚀 Deploy on Appwrite (Cloud Run)

This repository is now ready for container deployment on Appwrite using `gunicorn` and environment-based Django settings.

### Required Environment Variables

Set these in your Appwrite site/service environment:

- `PORT` = `3000` (recommended on Appwrite), or set `APPWRITE_FUNCTION_PORT` if provided by your runtime
- `DJANGO_SECRET_KEY` = `<a strong random string>`
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = `your-app-domain.com,.appwrite.global`
- `DJANGO_CSRF_TRUSTED_ORIGINS` = `https://your-app-domain.com,https://<your-appwrite-domain>`

### Build / Run behavior

The Docker container will:
1. install `requirements.txt`
2. run `collectstatic`
3. run `migrate`
4. start gunicorn on `0.0.0.0:${PORT:-${APPWRITE_FUNCTION_PORT:-3000}}`

---

## 📄 PDF Report

The system generates structured ledger statements including:

* Party Information
* Opening Balance
* Transaction Table
* Running Balance
* Closing Balance

---

## 👨‍💻 Author

**Divyanshu Tomar**  
Backend Developer | Django | REST APIs | System Design
