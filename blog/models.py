from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # This field will be populated by a call to timezone.now
    date_posted = models.DateTimeField(default=timezone.now)
    # If an user is deleted, also delete all his posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
