
from django.contrib import admin
from .models import Department, Employee, Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'seniority', 'department', 'role')
    ordering = ['id']
    list_filter = ['seniority', 'department', 'role']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
