import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from account.models import Profile

User = get_user_model()

@pytest.mark.django_db
def test_profile_is_auto_created(api_client, user_register_payload):
  url = reverse('register')
  response = api_client.post(url, user_register_payload, format='json')
  assert response.status_code == status.HTTP_201_CREATED
  assert User.objects.count() == 1
  assert User.objects.get().username == "johndoe"
  assert Profile.objects.count() == 1
  assert Profile.objects.filter(user__username="johndoe").exists()