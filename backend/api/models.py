from django.db import models

# Create your models here.


class TodoModel(models.Model):
    todo = models.CharField(max_length=10000)
    created_on = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo

