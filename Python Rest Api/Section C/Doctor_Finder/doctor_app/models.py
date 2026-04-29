from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    experience = models.IntegerField()
    fee = models.IntegerField()
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name