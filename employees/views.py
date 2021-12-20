
from rest_framework import viewsets

from employees.models import Department, Employee, Role
from employees.filters import DepartmentFilter, EmployeeFilter, RoleFilter
from employees.serializers import DepartmentSerializer, EmployeeSerializer, RoleSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows department to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_class = DepartmentFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employee to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_class = EmployeeFilter


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows role to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_class = RoleFilter
