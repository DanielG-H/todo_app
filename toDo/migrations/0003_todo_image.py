# Generated by Django 3.1.2 on 2020-12-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_auto_20201207_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(default='default_todo.jpg', upload_to='todo_pics'),
        ),
    ]