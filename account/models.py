from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

def profile_upload_to(instance, filename):
  return f"profiles/{instance.user.pk}/{filename}"

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)

  def __str__(self):
    return self.username
  
class Profile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile")
  full_name = models.CharField(max_length=255, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to=profile_upload_to, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return f"{self.user.username}'s profile"