from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Main path for the blog list
    path('', views.post_list, name='post_list'),
    
    # Path for viewing individual post details
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # Path for creating a new post (requires login)
    path('post/new/', views.post_new, name='post_new'),
    
    # Path for editing an existing post (requires login)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    # Admin interface URL
    path('admin/', admin.site.urls),
    
    # Account login/logout paths
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Include additional blog URLs
    path('', include('blog.urls')),  # This line includes other URLs in blog app if needed

    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
