# Neonumy Photo Album
A Django-based web application for uploading, managing, and viewing photos in an album format.

## Features

- Photo upload functionality
- Gallery view with thumbnails
- Photo detail pages
- REST API endpoints
- Admin interface for management

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Setup
1. Clone the repository:
 
   
2. Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Configure PostgreSQL:

  * Create a database

  * Update photo_album_project/settings.py with your credentials:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neonumy_album_db',
        'USER': 'neonumy_user',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
  }

5. Run migrations:
   python manage.py migrate

6. Create superuser (optional):
   python manage.py createsuperuser
   
8. Run development server:
python manage.py runserver


API Endpoints
 * GET /api/photos/ - List all photos

 * POST /api/photos/upload/ - Upload new photo

 * GET /api/photos/<id>/ - Get photo details

 * DELETE /api/photos/<id>/delete/ - Delete photo


