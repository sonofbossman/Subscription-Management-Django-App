from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
  description = models.TextField(blank=True, null=True, max_length=255)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Currency(models.Model):
  name = models.CharField(unique=True, max_length=50)
  code = models.CharField(unique=True, max_length=3)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.code

class Status(models.Model):
  name = models.CharField(max_length=50, unique=True, default="Active")
  description = models.TextField(null=True, blank=True, max_length=255)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Subscription(models.Model):
  service_name = models.CharField(max_length=100)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="subscriptions")
  billing_amount = models.DecimalField(max_digits=10, decimal_places=2)
  currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="subscriptions")
  date_subscribed = models.DateTimeField()
  next_billing_date = models.DateTimeField()
  status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="subscriptions")
  recurring = models.BooleanField(default=False)
  tags = models.ManyToManyField(Tag, related_name="subscriptions")
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.service_name