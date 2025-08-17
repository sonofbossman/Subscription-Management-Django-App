from django.contrib import admin
from account.models import Profile, CustomUser

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ('id', 'username', 'first_name', 'last_name', 
              'email', 'is_staff', 'is_active', 'last_login', 'date_joined'
              )
  list_filter = ('is_staff', 'is_active')
  search_fields = ('id', 'email', 'first_name', 'last_name', 'username')

class ProfileAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'full_name', 'date_of_birth', 'date_created', 'date_updated')
  search_fields = ('id', 'date_of_birth', 'full_name', 'user')
  list_filter = ('date_of_birth','date_created')

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)