from django.db import models


class UserEvent(models.Model):
    EVENT_CHOICES = [
        ("displayed", "Displayed"),
        ("acknowledged", "Acknowledged"),
        ("dismissed", "Dismissed"),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    url = models.URLField()
    comment = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.url} - {self.timestamp}"
