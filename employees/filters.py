
from django_filters.rest_framework import filters, FilterSet

from employees.models import Department, Employee, Role


class DepartmentFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Department
        fields = ['name']


class EmployeeFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    salary_gt = filters.NumberFilter(field_name='salary', lookup_expr='gt', label='Minimum salary')
    salary_lt = filters.NumberFilter(field_name='salary', lookup_expr='lt', label='Maximum salary')

    class Meta:
        model = Employee
        fields = ['name', 'salary_gt', 'salary_lt']


class RoleFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        fields = ['name']
