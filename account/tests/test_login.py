import pytest
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
def test_login_correct_credentials(api_client, user):
  url = reverse('login')
  payload = { "username": "testuser", "password": "Pass1234" }
  response = api_client.post(url, payload, format='json')

  assert response.status_code == status.HTTP_200_OK
  assert 'token' in response.data

@pytest.mark.django_db
def test_login_invalid_credentials(api_client, user):
  url = reverse('login')
  payload = { "username": "testuser3", "password": "Pass@1234" }
  response = api_client.post(url, payload, format='json')

  assert response.status_code == status.HTTP_400_BAD_REQUEST
  assert 'non_field_errors' in response.data