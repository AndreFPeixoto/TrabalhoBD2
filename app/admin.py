from django.contrib import admin
from .models import User, Group, Notice
from django.contrib.auth.models import Group as Groups

# Register your models here.
admin.site.unregister(Groups)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Notice)