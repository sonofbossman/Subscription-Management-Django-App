from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
import pytest

User = get_user_model()

@pytest.mark.django_db
def test_new_user_registration(api_client, user_register_payload):
  url = reverse('register')
  response = api_client.post(url, user_register_payload, format='json')
  assert response.status_code == status.HTTP_201_CREATED
  assert User.objects.count() == 1
  assert User.objects.get().username == "johndoe"
  user_details = response.data.get('user')
  message = response.data.get('message')
  assert 'token' in user_details
  assert message == "User registered successfully"

def test_register_existing_username(api_client, user):
  url = reverse('register')
  payload = {
    "username": user.username,
    "email": "john.doe@example.com", 
    "password": "PASS10$",
    "confirm_password": "PASS10$"
  }

  response = api_client.post(url, payload, format='json')
  assert response.status_code == status.HTTP_400_BAD_REQUEST
  assert 'username' in response.data

def test_register_existing_email(api_client, user):
  url = reverse('register')
  payload = {
    "username": "example_user",
    "email": user.email, 
    "password": "PASS10$",
    "confirm_password": "PASS10$"
  }

  response = api_client.post(url, payload, format='json')
  assert response.status_code == status.HTTP_400_BAD_REQUEST
  assert 'email' in response.data