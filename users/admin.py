from django.contrib import admin
from .models import  Role, Permission, RolePermetion, UserRoles,Transaction

# Register your models here.
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRoles)
admin.site.register(RolePermetion)
admin.site.register(Transaction)