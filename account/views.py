from rest_framework import generics, status
from rest_framework.response import Response
from account.serializers import RegisterSerializer, ProfileSerializer
from account.models import Profile
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(generics.CreateAPIView):
  """
  Register a new user and create token for the user.
  """

  queryset = get_user_model().objects.all()
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    response_data = { 
      "message": "User registered successfully",
      "user": serializer.data 
    } # customized response on successful creation
    return Response(data=response_data, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
  """
  Logout a user and destroy the user token.
  """
  permission_classes = [IsAuthenticated]

  def post(self, request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]

  def get_object(self):
    return self.request.user.profile
  
