from rest_framework import serializers
from django.contrib.auth import get_user_model
from subscription.models import Tag, Currency, Status, Subscription

class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = "__all__"
    read_only_fields = ['date_created', 'date_updated']

class CurrencySerializer(serializers.ModelSerializer):

  class Meta:
    model = Currency
    fields = "__all__"
    read_only_fields = ['date_created', 'date_updated']

class StatusSerializer(serializers.ModelSerializer):

  class Meta:
    model = Status
    fields = "__all__"
    read_only_fields = ['date_created', 'date_updated']

class SubscriptionSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(read_only=True)
  currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
  status = serializers.SlugRelatedField(slug_field="name", queryset=Status.objects.all())
  tags = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Tag.objects.all())

  class Meta:
    model = Subscription
    fields = "__all__"
    read_only_fields = ['date_created', 'date_updated']