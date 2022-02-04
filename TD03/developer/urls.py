from django.urls import path
from . import views
from .views import DevDetailVue, IndexView

app_name = 'developer'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:developer_id>', views.detail, name='detail'),
    path('<int:pk>', DevDetailVue.as_view(), name='detail'),
    path('delete/<int:developer_id>', views.delete, name='delete'),
    path('', IndexView.as_view(), name='index'),
    path('create', views.create, name='create'),
]
