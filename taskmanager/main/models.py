from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('title', max_length=50)
    task = models.TextField('task_descr')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = "tasks"