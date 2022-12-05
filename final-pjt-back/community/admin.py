from django.contrib import admin
from .models import Community, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Community)
