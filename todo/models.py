from django.db import models

# Create your models here.
from django.utils import timezone
 
class Todo(models.Model):
    title=models.CharField(max_length=350)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.title
