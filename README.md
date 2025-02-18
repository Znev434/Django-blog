# 📝 Django Blog – Portfolio Project

**Django Blog** is a simple blog application built with Django. It demonstrates full **CRUD** (Create, Read, Update, Delete) functionality, along with features such as **pagination**, **user messages**, and a **dark mode**.

## ✨ Features:
- 📝 Create, edit, and delete posts (Full CRUD)  
- 📄 Pagination (Post listing with pages)  
- 💬 User messages (e.g., "Post added!")  
- 🌙 Dark mode (Switch between light and dark themes)  
- 💻 Responsive design with custom CSS  

## 🛠️ Local Installation:  
```bash
git clone https://github.com/Znev434/Django-blog.git  
cd Django-blog  
python -m venv .venv  
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py createsuperuser  # (optional)  
python manage.py runserver

🌐 Usage:
🌍 Open: http://127.0.0.1:8000/
✏️ Add, edit, or delete posts
💬 Test user notifications and pagination