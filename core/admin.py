from django.contrib import admin
from core.models import UserProfileInfo
from list.models import Task
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Task)