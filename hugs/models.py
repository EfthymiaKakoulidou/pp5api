from django.db import models
from django.contrib.auth.models import User
from seecrets.models import Seecret


class Hug(models.Model):
    """
    Hug model, related to 'owner' and 'seecret'.
    'owner' is a User instance and 'seecret' is a Seecret instance.
    'unique_together' makes sure a user can't hug the same seecret twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hug = models.ForeignKey(
        Seecret, related_name='hugs', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'hug']

    def __str__(self):
        return f'{self.owner} {self.hug}'