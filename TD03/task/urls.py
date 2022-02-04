from django.urls import path
from .views import IndexView
from . import views

app_name = 'task'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('create', views.create, name='create'),
]
