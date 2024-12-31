from django.db import models
from users.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    is_spam = models.BooleanField(default=False)
