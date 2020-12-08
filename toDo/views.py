from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDo


def home(request):
    context = {
        "todos": ToDo.objects.all(),
    }
    return render(request, 'toDo/home.html', context)


class PostListView(ListView):
    model = ToDo
    template_name = 'toDo/home.html'
    context_object_name = 'todos'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = ToDo
    template_name = 'toDo/toDo-post_detail.html'
