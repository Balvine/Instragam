from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    """
    Class that contains profile details
    """
    pic = models.ImageField(upload_to='images/', blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()