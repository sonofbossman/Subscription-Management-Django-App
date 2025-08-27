from django.contrib import admin
from subscription.models import Tag, Currency, Status, Subscription
# Register your models here.

class TagAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'date_created', 'date_updated']
  list_filter = ['date_created']
  search_fields = ['name', 'description']

class CurrencyAdmin(admin.ModelAdmin):
  list_display = ['name', 'code', 'date_created', 'date_updated']
  list_filter = ['date_created']
  search_fields = ['name', 'code']

class StatusAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'date_created', 'date_updated']
  list_filter = ['date_created']
  search_fields = ['name', 'description']

class SubscriptionAdmin(admin.ModelAdmin):
  list_display = [
    'service_name', 'user', 'billing_amount', 'currency', 'date_subscribed',
    'next_billing_date', 'status', 'date_created', 'date_updated'
    ]
  list_filter = ['currency', 'date_created', 'recurring', 'status']
  search_fields = ['service_name', 'user', 'status', 'currency', 'tags']

admin.site.register(Tag, TagAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Subscription, SubscriptionAdmin)