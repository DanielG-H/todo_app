from django.urls import path
# from .views import PostListView
from . import views

urlpatterns = [
    path('', views.home, name='toDo-home')
]

