from django.urls import path, include
from .views import user_login, user_register, show_profile
app_name = "user_profile"
urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register),
    path('user/<int:pk>/', show_profile)
]
