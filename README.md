# Simple Django Blog + REST API

Features:
- Posts (title, description, image)
- Comments (author, text) related to a Post
- HTML pages: list, detail (with add comment), create post
- REST API (Django REST Framework): CRUD for posts & comments
- SQLite database, media upload support

## Quickstart

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional, for admin)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Open:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- API Root: http://127.0.0.1:8000/api/
- Posts API: http://127.0.0.1:8000/api/posts/
- Comments API: http://127.0.0.1:8000/api/comments/

### Notes
- Media uploads saved under `media/`. In production configure proper media serving.
- API allows read/write without auth for simplicity. Adjust `REST_FRAMEWORK` permissions for production.
