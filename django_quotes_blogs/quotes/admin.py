from django.contrib import admin

# Register your models here.

from .models import Quotes

admin.site.register(Quotes)