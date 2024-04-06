from django.db import models
from django.contrib.auth.models import User
from seecrets.models import Seecret


class Comment(models.Model):
    """
    Comment model, related to User and Seecret
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seecret = models.ForeignKey(Seecret, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content