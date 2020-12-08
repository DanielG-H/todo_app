from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDo


def home(request):
    context = {
        "todos": ToDo.objects.all(),
    }
    return render(request, 'toDo/home.html', context)


class ToDoListView(ListView):
    model = ToDo
    template_name = 'toDo/home.html'
    context_object_name = 'todos'
    ordering = ['-date_posted']


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = 'toDo/toDo-post_detail.html'


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    fields = ['title', 'description', 'status', 'due_date', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDo
    fields = ['title', 'description', 'status', 'due_date', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class ToDoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDo
    success_url = '/'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


def user_profile(request, pk):
    context = {
        'user': User.objects.filter(id=pk).first()
    }
    return render(request, 'users/user_profile.html', context)
