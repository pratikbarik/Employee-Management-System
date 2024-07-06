from django.contrib import admin
from .models import UserMaster
from .models import Leave
from .models import ApplyLeave
# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Leave)
admin.site.register(ApplyLeave)