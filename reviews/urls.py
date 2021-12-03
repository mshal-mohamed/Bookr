from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.book_list, name='book_list')
]
