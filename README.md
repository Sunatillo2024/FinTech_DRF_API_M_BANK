# 💳 FinTech API

[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)  
[![DRF](https://img.shields.io/badge/DRF-3.x-red)](https://www.django-rest-framework.org/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue)](https://www.postgresql.org/)  
[![Redis](https://img.shields.io/badge/Redis-6+-orange)](https://redis.io/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

FinTech API — bu **hamyonlar** va **tranzaksiyalarni** boshqarish uchun ishlab chiqilgan **RESTful API**.  
Ushbu loyiha **bank, wallet yoki payment tizimlari** uchun asosiy fundament sifatida xizmat qiladi.  

---

## 📑 Mazmun

- [🚀 Tez Start](#-tez-start)
- [⚙️ Arxitektura](#️-arxitektura)
- [📚 API Documentation](#-api-documentation)
- [🎯 API Foydalanish Misollari](#-api-foydalanish-misollari)
- [🧪 Testlar](#-testlar)
- [☁️ Deploy](#️-deploy)
- [🛠 Texnologiyalar](#-texnologiyalar)
- [👨‍💻 Author](#-author)

---

## 🚀 Tez Start

### 🔑 Oldin Shartlar

- **Python** 3.10+
- **PostgreSQL** 13+ (yoki SQLite development uchun)
- **Redis** 6+ (background tasks uchun)

---

### 1️⃣ Clone & Install

```bash
git clone https://github.com/yourusername/fintech-api.git
cd fintech-api
```

### 2️⃣ Virtual Muhit

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3️⃣ Kutubxonalar

```bash
pip install -r requirements.txt
```

### 4️⃣ Muhit O'zgaruvchilari

```bash
cp .env.example .env
```

`.env` faylni tahrirlang:

```env
DEBUG=True
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgres://user:password@localhost:5432/fintech
REDIS_URL=redis://localhost:6379/0
```

### 5️⃣ Database Migratsiya

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Serverni Ishga Tushirish

```bash
python manage.py runserver
```

👉 [http://localhost:8000](http://localhost:8000)

---

## ⚙️ Arxitektura

```mermaid
flowchart TD
    Client[🧑‍💻 Client] -->|HTTP/JSON| API[🌐 Django REST API]
    API -->|CRUD| DB[(PostgreSQL)]
    API -->|Cache/Tasks| Redis[(Redis)]
    API --> Auth[🔐 JWT Auth]
    API --> Wallet[💼 Wallet Service]
    API --> Txn[💸 Transaction Service]
    Wallet --> DB
    Txn --> DB
```

---

## 📚 API Documentation

### 🔐 Authentication

| Method | Endpoint                 | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/auth/api/register/`     | Yangi foydalanuvchi yaratish |
| POST   | `/auth/api/login/`        | Tizimga kirish           |
| POST   | `/auth/api/token/refresh/`| Token yangilash          |
| GET    | `/auth/api/profile/`      | Profil ma'lumotlari      |

---

### 💼 Wallet

| Method | Endpoint              | Description               |
|--------|------------------------|---------------------------|
| GET    | `/api/wallets/`        | Hamma hamyonlarni ko'rish |
| POST   | `/api/wallets/`        | Yangi hamyon yaratish     |
| GET    | `/api/wallets/{id}/`   | Hamyon ma'lumotlari       |
| PATCH  | `/api/wallets/{id}/`   | Hamyonni yangilash        |
| DELETE | `/api/wallets/{id}/`   | Hamyonni o'chirish        |

---

### 💸 Transactions

| Method | Endpoint                        | Description             |
|--------|----------------------------------|-------------------------|
| GET    | `/api/transactions/`             | Tranzaksiyalar ro'yxati |
| POST   | `/api/transactions/`             | Yangi tranzaksiya       |
| POST   | `/api/transactions/transfer/`    | Pul o'tkazish           |
| GET    | `/api/transactions/{id}/`        | Tranzaksiya tafsilotlari|

---

## 🎯 API Foydalanish Misollari

### Ro'yxatdan O'tish

```bash
curl -X POST http://localhost:8000/auth/api/register/   -H "Content-Type: application/json"   -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "password_confirm": "TestPass123!"
  }'
```

### Login Qilish

```bash
curl -X POST http://localhost:8000/auth/api/login/   -H "Content-Type: application/json"   -d '{
    "username": "testuser",
    "password": "TestPass123!"
  }'
```

### Hamyon Yaratish

```bash
curl -X POST http://localhost:8000/api/wallets/   -H "Content-Type: application/json"   -d '{
    "name": "My Wallet",
    "currency": "USD",
    "balance": 1000
  }'
```

---

## 🧪 Testlar

Unit testlarni ishga tushirish:

```bash
pytest
```

Coverage bilan:

```bash
pytest --cov=.
```

---

## ☁️ Deploy

Docker orqali:

```bash
docker-compose up --build -d
```

👉 Production uchun `DEBUG=False` qilib sozlashni unutmang.  

---

## 🛠 Texnologiyalar

- Django + DRF
- PostgreSQL / SQLite
- Redis + Celery
- Docker + Docker Compose
- Pytest (testlar uchun)

---

## 👨‍💻 Author

Created by [Your Name](https://github.com/yourusername)  

Licensed under [MIT](LICENSE) ⚖️
