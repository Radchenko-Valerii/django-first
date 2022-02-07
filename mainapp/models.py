from django.db import models


class Task(models.Model):
    title = models.CharField('name', max_length=56)
    task = models.TextField('lol')

    def __str__(self):
        return self.title
