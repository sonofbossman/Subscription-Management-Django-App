import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
  return APIClient()

@pytest.fixture
def user_register_payload():
  return {
    "username": "johndoe",
    "email": "john.doe@example.com", 
    "password": "PASSWORD10$",
    "confirm_password": "PASSWORD10$"
  }

@pytest.fixture
def user(db):
  return User.objects.create_user(
    username="testuser", 
    email="test@user.com",
    password="Pass1234"
  )