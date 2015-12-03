from django.contrib import admin

# Register your models here.
from funcov.models import UserProfile, Coverpoint, Covergroup, Parameter, ParameterChoice

admin.site.register(UserProfile)
admin.site.register(Coverpoint)
admin.site.register(Covergroup)
admin.site.register(Parameter)
admin.site.register(ParameterChoice)
