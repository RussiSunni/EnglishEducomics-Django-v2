from django.contrib import admin

from .models import Stages, Users, UserStages

# Register your models here.


admin.site.register(Stages)
admin.site.register(UserStages)
admin.site.register(Users)
