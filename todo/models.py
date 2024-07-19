from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=100, null=True, blank=True)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)

    def is_overdue(self, current_time=None):
        if not self.due_at:
            return False
        if not current_time:
            current_time = timezone.now()
        return current_time > self.due_at