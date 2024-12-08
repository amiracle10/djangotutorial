"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Root URL for the blog
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail
    path('post/new/', views.post_new, name='post_new'),  # New post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # Edit post
    path('admin/', admin.site.urls),  # Admin site
    path('accounts/login/', LoginView.as_view(), name='login'),  # Login view
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Logout view
]

