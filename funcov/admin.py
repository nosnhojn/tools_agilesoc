from django.contrib import admin

# Register your models here.
from funcov.models import UserProfile, Coverpoint

admin.site.register(UserProfile)
admin.site.register(Coverpoint)
