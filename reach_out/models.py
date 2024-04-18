from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Reach_out(models.Model):
    """
    Reach_out model, related to User and Profile
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reach_out_to = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
