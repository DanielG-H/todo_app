from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .enums import StatusList


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.CharField(default=StatusList.TODO, choices=StatusList.choices(), max_length=255)
    image = models.ImageField(default="default_todo.jpg", upload_to="todo_pics")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('toDo-post_detail', kwargs={'pk': self.pk})
