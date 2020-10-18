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
        
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_profile_by_id(cls, id):
        user_profile = Profile.objects.get(user=id)
        return user_profile

    @classmethod
    def get_profile_by_username(cls, user):
        profile_info = cls.objects.filter(user__contains=user)

    