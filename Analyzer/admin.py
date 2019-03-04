from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.general_expenses)
admin.site.register(models.mandatory_expenses)
admin.site.register(models.debts)
admin.site.register(models.user_profile)
