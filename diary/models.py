from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    """
    Diary model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.content}'
