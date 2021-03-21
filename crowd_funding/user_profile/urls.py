from django.urls import path, include
from .views import user_login, user_register
app_name = "user_profile"
urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register),
]
