from django.db import models
from django.utils import timezone


class Career(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(default=timezone.now, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.title}"
