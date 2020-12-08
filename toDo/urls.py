from django.urls import path
from .views import ToDoListView, ToDoDetailView, ToDoCreateView, ToDoUpdateView,  ToDoDeleteView
from . import views

urlpatterns = [
    path('', ToDoListView.as_view(), name='toDo-home'),
    path('toDo/<int:pk>', ToDoDetailView.as_view(), name="toDo-post_detail"),
    path('toDo/new/', ToDoCreateView.as_view(), name="toDo_create"),
    path('toDo/<int:pk>/update/', ToDoUpdateView.as_view(), name="toDo_update"),
    path('toDo/<int:pk>/delete/', ToDoDeleteView.as_view(), name="toDo_delete"),
    path('toDo/<int:pk>/user_profile', views.user_profile, name="user_profile")
]
