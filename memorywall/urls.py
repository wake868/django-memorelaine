# urls.py -> memorywall
from django.urls import path
from . import views

app_name = 'memorywall'

urlpatterns = [
    path('', views.home, name='home'),
]