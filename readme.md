# XMini

A full-stack social media web application built with Django. XMini is a lightweight X/Twitter-style platform where users can create accounts, publish posts, upload images, search posts and users, view profiles, and manage their own content.

## Features

* User registration and authentication
* Login and logout
* Create, edit, and delete posts
* Image uploads
* User profile pages
* Search posts by text or username
* User-specific post permissions
* Django admin interface
* Form validation
* Database migrations
* Automated tests
* Responsive Bootstrap-based interface
* Dark-themed UI

## Tech Stack

* **Backend:** Django 6.1.1
* **Language:** Python
* **Database:** SQLite
* **Frontend:** HTML, CSS, Bootstrap
* **Image Processing:** Pillow
* **Development Tools:** VS Code, Git, GitHub

## Project Structure

```text
XMini/
├── XMini/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── x/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── registration/
│   ├── layout.html
│   ├── x_list.html
│   ├── x_form.html
│   ├── x_delete.html
│   └── user_profile.html
├── static/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AnanyaPanwar/XMini.git
cd XMini
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If you use `uv`:

```powershell
uv pip install -r requirements.txt
```

Or with standard pip:

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file for local development if you are using environment variables for Django settings.

Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Do not commit `.env` to GitHub.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Run tests

```powershell
python manage.py test
```

### 7. Start the development server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/x/
```

## Testing

The project includes automated tests covering areas such as:

* Post creation
* Post editing
* Post deletion
* Search
* Authentication requirements
* User permissions
* Profile pages
* Model behavior

Run the test suite with:

```powershell
python manage.py test
```

## Security

Sensitive and local development files are excluded from version control through `.gitignore`, including:

* `.env`
* `.venv/`
* `db.sqlite3`
* `media/`
* `__pycache__/`

For production deployment, configure a secure secret key, disable debug mode, configure allowed hosts, and use a production-ready database and deployment configuration.

## What I Learned

Building XMini provided practical experience with:

* Django project and app architecture
* Django models and relationships
* Model forms and validation
* Authentication and authorization
* CRUD operations
* File uploads
* Django ORM and database queries
* Search functionality
* Template inheritance
* Django admin
* Automated testing
* Git and GitHub workflows
* Basic application security

## Future Improvements

Possible future improvements include:

* Following and follower functionality
* Likes and comments
* Pagination
* Notifications
* User profile customization
* REST API
* Deployment to a cloud platform
* PostgreSQL support

## Author

**Ananya Panwar**

GitHub: https://github.com/AnanyaPanwar

## License

This project is currently intended as a portfolio and learning project.
