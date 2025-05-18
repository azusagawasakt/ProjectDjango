from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_entry, name='create_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='diary/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
