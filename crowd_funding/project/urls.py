from django.urls import path
from .views import (
    add_project,
    show_project,
)
app_name = "project"
urlpatterns = [
    path('add/', add_project, name='add_project'),
    path('show/<int:pk>', show_project, name='show_project'),

]
