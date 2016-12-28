from django.db import models
from django.utils import timezone


class Pattern(models.Model):
    maker = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    material = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name
