from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

class AccountTests(APITestCase):
  def test_register(self):
    """
    Ensure we can create a new account object.
    """
    url = reverse('register')
    data = {
    "username": "johndoe",
    "email": "john.doe@example.com", 
    "password": "PASSWORD10$",
    "confirm_password": "PASSWORD10$"
    }

    response = self.client.post(url, data, format='json')
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(get_user_model().objects.count(), 1)
    self.assertEqual(get_user_model().objects.get().username, "johndoe")

