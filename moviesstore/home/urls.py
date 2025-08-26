from django.urls import search
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
]