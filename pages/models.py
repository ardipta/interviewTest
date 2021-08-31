from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
