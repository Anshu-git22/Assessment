from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=150)
    bio = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username