from django.contrib import admin

# Register your models here.
from .models import RUserdata, Notes

# Register your models here.
admin.site.register(RUserdata)
admin.site.register(Notes)
