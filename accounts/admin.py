from django.contrib import admin
from .models import Enterprise, AdminUser, Employee, Tenant

# Register your models here.
admin.site.register(Enterprise)
admin.site.register(AdminUser)
admin.site.register(Employee)
admin.site.register(Tenant)