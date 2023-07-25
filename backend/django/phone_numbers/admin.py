from django.contrib import admin
from .models import PhoneNumber

# Register your models here.
class PhoneNumberAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhoneNumber, PhoneNumberAdmin)
