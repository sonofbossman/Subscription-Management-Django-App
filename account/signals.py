from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from account.models import Profile

# creates a token when a user is first created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
  if created:
    Token.objects.create(user=instance)

# ensures a profile exists for every user and is saved whenever user is updated.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def manage_profile(sender, instance, **kwargs):
  Profile.objects.update_or_create(
    user=instance,
    defaults={
      "full_name": f"{instance.first_name} {instance.last_name}".strip()
    }
  )