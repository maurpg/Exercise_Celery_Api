from django.urls import path
from . import views

urlpatterns = [
    path('', views.Search.as_view() , name = 'search_movie'),
]