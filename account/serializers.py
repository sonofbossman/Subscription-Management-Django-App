from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True, style={'input-type': 'password'})
  token = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = get_user_model()
    fields = ['username', 'email', 'password', 'confirm_password', 'token']
    extra_kwargs = {
      'password': { 'write_only': True }, # remove password field from API response
      'email': { 'required': True, 
                'validators': [UniqueValidator(queryset=get_user_model().objects.all())] }, # email field should be unique and must be included
    }
  
  def get_token(self, obj):
    token, _ = Token.objects.get_or_create(user=obj)
    return token.key
  
  def create(self, validated_data):
    password = validated_data.get('password', None)
    confirm_password = validated_data.pop('confirm_password', None) # don't save the confirm_password field
    if password and confirm_password:
      if password != confirm_password:
        raise serializers.ValidationError({ 'error': 'Password and confirm password did not match' })
      user = get_user_model().objects.create_user(**validated_data)
      return user
    raise serializers.ValidationError({ 'error': 'Password and confirm password must be provided' })

class ProfileSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(read_only=True)
  first_name = serializers.CharField(source="user.first_name")
  last_name = serializers.CharField(source="user.last_name")
  email = serializers.EmailField(source="user.email")
  date_joined = serializers.DateTimeField(source="user.date_joined")
  is_active = serializers.BooleanField(source="user.is_active")

  class Meta:
    model = Profile
    fields = ['id', 'user', 'first_name', 'last_name', 
              'full_name', 'email', 'profile_photo', 
              'is_active', 'date_of_birth', 'date_joined', 'date_updated'
            ]
    read_only_fields = ['id', 'date_updated', 'date_joined', 'full_name', 'is_active']
  
  def update(self, instance, validated_data):
    # Extract nested user data
    user_data = validated_data.pop('user', {})
    # Expunge read_only fields
    user_data.pop("date_joined", None)
    user_data.pop("is_active", None)

    # Update User fields
    user = instance.user
    for attr, value in user_data.items():
      if value is not None:
        setattr(user, attr, value)
    user.save()

    # Update Profile fields
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    # Update the full_name field
    instance.full_name = f"{user.first_name} {user.last_name}".strip()
    instance.save()

    return instance