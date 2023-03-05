from django.db import models

# Create your models here.


class Insurance(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name
