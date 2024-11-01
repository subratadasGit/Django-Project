
# Django Project with UV and Multiple Apps

This is a sample Django project setup guide with `uv`, a virtual environment, and multiple apps (`myapp` and `mysite`). The project is structured to keep URLs, views, templates, and static files well-organized.

## Requirements

- Python 3.x
- `uv` package
- Django

## Setup Guide

### Step 1: Install UV
Install the `uv` package if it’s not already installed:
```bash
pip install uv
```

### Step 2: Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv uv
```
Activate it:
- **Windows**: `uv\Scripts\activate`
- **Mac/Linux**: `source uv/bin/activate`

### Step 3: Create a Django Project
Initialize the Django project by running:
```bash
django-admin startproject mysite djangotutorial
```

### Step 4: Create and Configure Apps
1. Create `myapp` and `mysite` apps:
   ```bash
   python manage.py startapp myapp
   python manage.py startapp mysite
   ```

2. Add the apps to the `INSTALLED_APPS` list in `djangotutorial/settings.py`:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'myapp',
       'mysite',
   ]
   ```

### Step 5: Set Up URLs

1. **Project URLs** (`djangotutorial/urls.py`):
   ```python
   from django.contrib import admin
   from django.urls import path, include
   from myapp import views as myapp_views
   from mysite import views as mysite_views

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', myapp_views.home, name='home'),        # Main home page
       path('about/', myapp_views.about, name='about'), # About page in myapp
       path('contact/', mysite_views.contact, name='contact'), # Contact page in mysite
       path('myapp/', include('myapp.urls')),           # Includes URLs from myapp
   ]
   ```

2. **App URLs**:
   - **myapp/urls.py**:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.dj_app_home, name='dj_app_home'),
         # Additional routes if needed
     ]
     ```

3. **Views**:
   - **myapp/views.py**:
     ```python
     from django.shortcuts import render

     def home(request):
         return render(request, 'myapp/dj_app.html')

     def about(request):
         return render(request, 'about.html')
     ```

   - **mysite/views.py**:
     ```python
     from django.shortcuts import render

     def contact(request):
         return render(request, 'contact.html')
     ```

### Step 6: Templates and Static Files

Organize templates within each app's `templates` folder. Make sure `TEMPLATES` and `STATICFILES_DIRS` in `settings.py` are configured as follows:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Global template folder
        ...
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### Step 7: Run the Server
After setup, start the development server:
```bash
python manage.py runserver
```

## Project Structure Overview

```
mysite/
├── djangotutorial/
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL routing
├── myapp/                  # App: myapp
│   ├── templates/
│   │   └── myapp/
│   │       └── dj_app.html
│   ├── views.py
│   ├── urls.py
├── mysite/                 # App: mysite
│   ├── views.py
│   ├── urls.py
├── templates/              # Global templates
│   ├── about.html
│   ├── contact.html
└── static/                 # Global static files
```

## Troubleshooting

- **404 Errors (e.g., `/favicon.ico`, `/chai`, `/myapp`)**:
  - Make sure URLs are defined in `urls.py` for the requested paths.
  - If `favicon.ico` is missing, add it in the `static` folder or ignore it.

- **Template Not Found**:
  - Check that template names in `render()` match actual filenames and paths.

- **Static Files Not Loading**:
  - Ensure that `STATICFILES_DIRS` is configured correctly, and `collectstatic` is run for production.

## License

This project is licensed under the MIT License.
