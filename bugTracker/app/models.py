from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=600)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
