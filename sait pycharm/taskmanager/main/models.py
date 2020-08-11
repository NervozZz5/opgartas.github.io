from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=70)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
'''
admin 
123456789
'''