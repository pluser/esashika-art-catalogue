import os.path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
