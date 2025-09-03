# 💳 FinTech API

FinTech API — bu Django va Django REST Framework asosida yozilgan hamyon va tranzaksiya boshqaruv tizimi.  

---

## 🚀 Tez Start

### 🔑 Oldin Shartlar

- **Python** 3.10+
- **PostgreSQL** 13+ (yoki SQLite development uchun)
- **Redis** 6+ (background tasks uchun)

---

### 1️⃣ Loyihani Clone Qilish

```bash
git clone https://github.com/yourusername/fintech-api.git
cd fintech-api
```

---

### 2️⃣ Virtual Muhit Yarating

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# yoki
.venv\Scripts\activate  # Windows
```

---

### 3️⃣ Kutubxonalarni O'rnatish

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Muhit O'zgaruvchilarini Sozlash

```bash
cp .env.example .env
```

`.env` faylni tahrirlang:

```env
DEBUG=True
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
```

---

### 5️⃣ Ma'lumotlar Bazasini Sozlash

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### 6️⃣ Serverni Ishga Tushirish

```bash
python manage.py runserver
```

👉 Loyihaga kirish: [http://localhost:8000](http://localhost:8000)

---

## 📚 API Documentation

### 🔐 Authentication Endpoints

| Method | Endpoint                 | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/auth/api/register/`     | Yangi foydalanuvchi yaratish |
| POST   | `/auth/api/login/`        | Tizimga kirish           |
| POST   | `/auth/api/token/refresh/`| Token yangilash          |
| GET    | `/auth/api/profile/`      | Profil ma'lumotlari      |

---

### 💼 Wallet Endpoints

| Method | Endpoint              | Description               |
|--------|------------------------|---------------------------|
| GET    | `/api/wallets/`        | Hamma hamyonlarni ko'rish |
| POST   | `/api/wallets/`        | Yangi hamyon yaratish     |
| GET    | `/api/wallets/{id}/`   | Hamyon ma'lumotlari       |
| PATCH  | `/api/wallets/{id}/`   | Hamyonni yangilash        |
| DELETE | `/api/wallets/{id}/`   | Hamyonni o'chirish        |

---

### 💸 Transaction Endpoints

| Method | Endpoint                        | Description             |
|--------|----------------------------------|-------------------------|
| GET    | `/api/transactions/`             | Tranzaksiyalar ro'yxati |
| POST   | `/api/transactions/`             | Yangi tranzaksiya       |
| POST   | `/api/transactions/transfer/`    | Pul o'tkazish           |
| GET    | `/api/transactions/{id}/`        | Tranzaksiya tafsilotlari|

---

## 🎯 API Foydalanish Misollari

### 🔹 Ro'yxatdan O'tish

```bash
curl -X POST http://localhost:8000/auth/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "password_confirm": "TestPass123!"
  }'
```

---

### 🔹 Login Qilish

```bash
curl -X POST http://localhost:8000/auth/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPass123!"
  }'
```

---

### 🔹 Yangi Hamyon Yaratish

```bash
curl -X POST http://localhost:8000/api/wallets/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Wallet",
    "currency": "USD",
    "balance": 1000
  }'
```

---

## 🛠 Texnologiyalar

- Django
- Django REST Framework
- PostgreSQL / SQLite
- Redis
- Celery

---

## 👨‍💻 Author

[Your Name](https://github.com/Sunatillo2024)

---
