from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100, null=True, blank=True)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)