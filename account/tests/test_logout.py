import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_logout(api_client, user):
  url = reverse('logout')
  token = Token.objects.get(user=user)
  api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
  response = api_client.post(url)
  assert response.status_code == status.HTTP_200_OK
  assert not Token.objects.filter(user=user).exists()