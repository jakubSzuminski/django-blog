# django-blog
(Back-end + Front-end) Blog created with HTML, CSS, JavaScript and Python, Django.
**Users can** 
- register, 
- login, 
- comment on posts, 
- search through the posts by text and by selecting tags

Posts can only be added by the admins in the Django admin panel.

# Setup 
To replicate this project you need to

## 1. Have:
- Python (with pip)
- Django (for this project 4.06 version was used)
- django-taggit (for this project 3.0.0 version was used)

## 2. Create a Django project
```
django-admin startproject Blog
```

## 3. Create 2 Django applications
One for most of our functionalities:
```
python manage.py startapp main
```
One connected to user system (register/login)
```
python manage.py startapp users
```

### Add these apps to the Django settings
```
INSTALLED_APPS = [
  ...,
  
  'main',
  'users',
  'taggit',
]
```

### Add additional settings at the bottom of your file
```
TAGGIT_CASE_INSENSITIVE = True
LOGIN_REDIRECT_URL = 'home-page'
```

## 4. Create the necessary models and forms
Based on the files in the repository, update these:
### main/models.py 
Create "Post" and "Comment" models. 
### main/forms.py
Create a "CreateCommentForm" based on the Comment model.
### users/forms.py
Create a "UserRegisterForm" based on UserCreationForm and add email field.
### Then run the migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Then you can register these models in the main/admin.py
```
from .models import Post, Comment
admin.site.register(Post)
admin.site.register(Comment)
```

## 5. Setup static files
5.1. Copy all the scripts (from the 'scripts' folder in the repository) to *main/static/main/scripts/*

5.2. Copy all the scss files (from the 'styles' folder in the repository) to *main/static/main/styles/*

**Keep in mind that these files are .scss so you will need to click "Watch SASS" in your VSCODE in order for them to generate a proper CSS code**

## 6. Setup all the HTML templates
6.1 Copy all the HTML files (from the 'main HTML templates' folder in the repository) to *main/templates/main/*

6.2 Copy all the HTML files (from the 'users HTML templates' folder in the repository) to *users/templates/users/*

## 7. Setup urls.py
Add all the url paths from the urls.py file in the repository.

## 8. Add all the views 
8.1 Copy the main/views.py content to your main/views.py file 

8.2 Copy the users/views.py content to your users/views.py file

## 9. You can add posts with basic HTML tags based on how-to-create-posts file in the repository.
Add a few posts in the admin panel.

## 10. Run the server & test
After you've added a few posts you can start testing.
