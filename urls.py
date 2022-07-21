from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

#importing views
#main site views
from main.views import home, post_detail, search_posts, contact, comment_delete

#user views
from users.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name = 'home-page'), 
    
    path('posts/<slug:slug>', post_detail, name = 'post-detail'),
    path('comment-delete/<int:comment_id>', comment_delete, name = 'comment-delete'),
    path('search-posts', csrf_exempt(search_posts), name = 'search-posts'),
    path('category/<slug:tag_slug>', home, name = 'category'),

    path('contact/', contact, name = 'contact-page'),

    path('register/', register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
]
