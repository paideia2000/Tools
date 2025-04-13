from django.contrib import admin
from .models import Users, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Users)

