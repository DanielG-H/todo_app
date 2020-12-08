from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Status(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Status"

    def __str__(self):
        return self.title


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.ForeignKey(Status, verbose_name="Status", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post_detail', kwargs={'pk': self.pk})
