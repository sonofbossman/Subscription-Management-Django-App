from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)

  def __str__(self):
    return super().__str__()
  
class Profile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
  full_name = models.CharField(max_length=255, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return f"{self.user.username}'s profile"