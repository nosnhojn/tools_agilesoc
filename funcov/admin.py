from django.contrib import admin

# Register your models here.
from funcov.models import UserProfile

admin.site.register(UserProfile)
