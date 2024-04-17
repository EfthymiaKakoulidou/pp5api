from django.db import models
from django.contrib.auth.models import User
from reach_out.models import Reach_out


class Reach_out_comment(models.Model):
    """
    Comment model, related to User and Seecret
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reach_out = models.ForeignKey(
        Reach_out,
        on_delete=models.CASCADE,
        blank=False,
        null=False
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reach_out_comment_content = models.TextField()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.reach_out_comment_content
