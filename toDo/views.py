from django.shortcuts import render
from django.views.generic import ListView


todos = [
    {
        'author': 'daniel garcia',
        'title': 'my first to-do',
        'description': 'a nice to-do',
        'date_posted': '7/12/20',
        'due_date': '8/12/20',
    },
]


def home(request):
    context = {
        "todos": todos,
    }
    return render(request, 'toDo/home.html', context)


# class PostListView(ListView):
#     model = to_do
#     template_name = html
#     context_object_name = 'todos'
#     ordering = ['-date_posted']
