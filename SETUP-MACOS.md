# Setup Guide - macOS

Terminal app သုံးပါ။ Command အားလုံးမှာ `python3` သုံးပါ။

---

## လိုအပ်ချက်

- Python 3.10 သို့မဟုတ် 3.11
- [python.org/downloads](https://www.python.org/downloads/) သို့ Homebrew နဲ့ install:
  ```bash
  brew install python
  ```

Version စစ်ရန်:

```bash
python3 --version
```

---

## Setup (အဆင့် ၆)

### အဆင့် ၁ - Project folder ထဲဝင်ပါ

`manage.py` file ရှိတဲ့ folder က project root ဖြစ်ပါတယ်။

```bash
cd /path/to/blog
```

---

### အဆင့် ၂ - Virtual Environment ဖန်တီးပြီး ဖွင့်ပါ

```bash
python3 -m venv .venv
source .venv/bin/activate
```

`(.venv)` လို့ terminal မှာ ပေါ်လာရင် အောင်မြင်ပါပြီ။

venv ပိတ်ရန်:

```bash
deactivate
```

---

### အဆင့် ၃ - Packages install လုပ်ပါ

venv activate လုပ်ထားပြီးမှ run ပါ:

```bash
pip install -r requirements.txt
```

---

### အဆင့် ၄ - `.env` file ပြင်ဆင်ပါ

```bash
cp .env.example .env
```

`.env` file ကို text editor နဲ့ ဖွင့်ပြီး ပြင်ပါ:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

SECRET_KEY ထုတ်ရန်:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> `.env` file က git ထဲ မထည့်ပါနဲ့ - password, secret key ပါဝင်ပါတယ်။

**Forgot Password (Email) အတွက် Gmail App Password:**

1. Google Account > Security > 2-Step Verification ဖွင့်ပါ
2. App Passwords > Mail ရွေးပြီး password ထုတ်ပါ
3. ထုတ်ထားတဲ့ password ကို `EMAIL_HOST_PASSWORD` ထဲ ထည့်ပါ

---

### အဆင့် ၅ - Database setup

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

Username, Email, Password ထည့်ပြီး admin account ဖန်တီးပါ။

---

### အဆင့် ၆ - Server စတင်ပါ

```bash
python3 manage.py runserver
```

Browser မှာ ဖွင့်ပါ:

- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Server ရပ်ရန်: `Ctrl + C`

---

## Setup ပြီး

---

## ပြဿနာတွေ့ရင်

**`'python3' command not found`**

```bash
brew install python
```

**`ModuleNotFoundError`**

```bash
pip install python-dotenv django-jazzmin django-pwa pillow
```

**Email မပို့နိုင်ဘူး**

`.env` ထဲက email/password မှန်မှု စစ်ပါ။ Gmail App Password သုံးပါ။

**Port 8000 already in use**

```bash
python3 manage.py runserver 8080
```
