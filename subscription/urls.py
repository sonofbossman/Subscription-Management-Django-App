from django.urls import path, include
from rest_framework import routers
from subscription.views import (
  SubscriptionViewSet, CurrencyViewSet, StatusViewSet,
  TagViewSet
)

router = routers.DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'status', StatusViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
