...

INSTALLED_APPS = [
 ...
    'main', #adding my main blog application 
    'taggit', #used for "tags" in Post model
    'users', #app for the user model and login/register
]

...

#ADDITIONAL SETTINGS
TAGGIT_CASE_INSENSITIVE = True
LOGIN_REDIRECT_URL = 'home-page' 
