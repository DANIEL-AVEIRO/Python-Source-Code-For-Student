# API Routes (URL List)

Blog Project ရဲ့ route (URL) အားလုံး စာရင်းဖြစ်ပါတယ်။
Server run ပြီးရင် base URL: **http://127.0.0.1:8000**

> **Auth** - `Yes` ဆိုရင် login လုပ်ထားရမယ်။ `No` ဆိုရင် login မလိုပါ။

---

## Home

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/` | `home` | No | Homepage - active post list + search |
| GET | `/?search=keyword` | `home` | No | Post search (title, content, category, author) |

---

## Post

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/post/list/` | `post_list` | Yes | Post list page |
| GET | `/post/list/?search=keyword` | `post_list` | Yes | Post search by title |
| GET | `/post/create/` | `post_create` | Yes | Post create form |
| POST | `/post/create/` | `post_create` | Yes | Post အသစ် save |
| GET | `/post/update/<uuid>/` | `post_update` | Yes | Post edit form |
| POST | `/post/update/<uuid>/` | `post_update` | Yes | Post update save |
| GET | `/post/delete/<uuid>/` | `post_delete` | Yes | Post delete |
| GET | `/post/toggle/<uuid>/` | `post_toggle` | Yes | Post active/inactive toggle |
| GET | `/post/details/<uuid>/` | `post_details` | Yes | Post detail + comments |

**POST `/post/create/` & `/post/update/<uuid>/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `title` | text | Yes |
| `content` | text | Yes |
| `category` | select (category id) | Yes |
| `image` | file | create: Yes / update: No |

---

## Category

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/category/list/` | `category_list` | Yes | Category list |
| GET | `/category/create/` | `category_create` | Yes | Category create form |
| POST | `/category/create/` | `category_create` | Yes | Category အသစ် save |
| GET | `/category/update/<uuid>/` | `category_update` | Yes | Category edit form |
| POST | `/category/update/<uuid>/` | `category_update` | Yes | Category update save |
| GET | `/category/delete/<uuid>/` | `category_delete` | Yes | Category delete |

**POST `/category/create/` & `/category/update/<uuid>/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `name` | text | Yes |

---

## Comment

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| POST | `/comment/create/<post_uuid>/` | `comment_create` | Yes | Post အောက်မှာ comment ရေးခြင်း |
| GET | `/comment/delete/<uuid>/` | `comment_delete` | Yes | Comment delete |

**POST `/comment/create/<post_uuid>/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `content` | text | Yes |

---

## Authentication

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/login/` | `login` | No | Login page |
| POST | `/login/` | `login` | No | Login submit |
| GET | `/logout/` | `logout` | No | Logout |
| GET | `/register/` | `register` | No | Register page |
| POST | `/register/` | `register` | No | Register submit |

**POST `/login/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `username` | text | Yes |
| `password` | password | Yes |

**POST `/register/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `username` | text | Yes |
| `email` | email | Yes |
| `password` | password | Yes |
| `confirm_password` | password | Yes |

---

## Profile

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/profile/` | `profile` | Yes | Profile page |
| POST | `/profile/` | `profile` | Yes | Profile update save |

**POST `/profile/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `username` | text | Yes |
| `email` | email | Yes |
| `bio` | text | No |
| `phone` | text | No |
| `address` | text | No |
| `profile` | file (image) | No |

---

## Forgot Password

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET | `/forgot-password/` | `forgot_password` | No | Forgot password page |
| POST | `/forgot-password/` | `forgot_password` | No | Reset link email ပို့ခြင်း |
| GET | `/reset-password/<token>/` | `reset_password` | No | New password form |
| POST | `/reset-password/<token>/` | `reset_password` | No | Password reset save |

**POST `/forgot-password/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `email` | email | Yes |

**POST `/reset-password/<token>/` fields:**

| Field | Type | Required |
|-------|------|----------|
| `new_password` | password | Yes |
| `confirm_new_password` | password | Yes |

---

## Admin

| Method | URL | Name | Auth | Description |
|--------|-----|------|------|-------------|
| GET/POST | `/admin/` | - | Yes (superuser) | Django Admin Panel |

---

## PWA (Progressive Web App)

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/manifest.json` | PWA manifest file |
| GET | `/serviceworker.js` | Service worker file |

---

## URL Parameter Notes

| Parameter | Format | Example |
|-----------|--------|---------|
| `<uuid>` | UUID v4 | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `<token>` | UUID string | password reset token |
| `<post_uuid>` | UUID v4 | post id for comment |

---

## Template မှာ URL သုံးနည်း

Django template ထဲမှာ route name နဲ့ link ထုတ်နည်း:

```html
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'post_details' pk=post.id %}">View Post</a>
<a href="{% url 'post_update' pk=post.id %}">Edit</a>
<a href="{% url 'reset_password' token=token %}">Reset Password</a>
```

---

## Route File Location

Route definitions: [`blog/urls.py`](blog/urls.py)
View functions: [`core/views.py`](core/views.py)
