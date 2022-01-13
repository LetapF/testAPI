from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_created')
    date_created = models.DateTimeField(auto_now_add=True)
    user_updated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_updated')
    date_updated = models.DateTimeField(auto_now=True)
