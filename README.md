BufferSpot

BufferSpot is a modern and elegant tech blogging platform built with Django. It enables users to write, read, and explore blog posts on technology topics like Data Structures, OOPs, DBMS, and more. It includes live preview while writing, user authentication, analytics, search functionality, and a clean UI/UX.

Features

- Create, read, update, and delete blog posts (CRUD)
- Live preview while writing posts
- Rich text formatting support (with line breaks and spacing)
- User registration and login/logout
- Author profiles with profile picture
- Post view count and trending posts
- Top authors based on post count
- Full-text search (title and content)
- Pagination and responsive design
- Announcements, Events, Resources, Contact page
- Dark/Light mode toggle
- Admin interface for managing content

Tech Stack

- Backend: Django 5+
- Frontend: Bootstrap 4, HTML5, CSS3
- Database: SQLite (default, can switch to PostgreSQL)
- Authentication: Django built-in auth system

Getting Started

Prerequisites

- Python 3.9+
- pip
- Git

Installation

Clone the repository
```
git clone https://github.com/your-username/bufferspot.git
cd bufferspot
```

Create a virtual environment
```
python -m venv env
source env/bin/activate
```
(on Windows: env\Scripts\activate)

Install dependencies
```
pip install -r requirements.txt
```
Run migrations
```
python manage.py makemigration
python manage.py migrate
```
Create superuser (admin)
```
python manage.py createsuperuser
```
Run development server
```
python manage.py runserver
```

Search Functionality

The search bar dynamically filters posts based on title or content using:
Q(title__icontains=query) | Q(content__icontains=query)

Analytics

- Each post tracks views (excluding author views)
- Top trending posts can be shown based on views
- Top authors displayed based on number of posts

Live Preview (Post Create/Edit)

Live preview updates instantly as you type using JavaScript like:
function updatePreview() {
    ...
}

Contact

Email: noorafikjalaludeen2204@gmail.com

License

This project is licensed under the MIT License. See the LICENSE file for details.
