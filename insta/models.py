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
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()