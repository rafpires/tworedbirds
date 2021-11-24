
from django.db import models


class Role(models.Model):
    id = models.AutoField('PK', primary_key=True, db_column='id_role')
    name = models.CharField('Name', db_column='nm_role', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Department(models.Model):
    id = models.AutoField('PK', primary_key=True, db_column='id_department')
    name = models.CharField('Name', db_column='nm_department', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Employee(models.Model):
    id = models.AutoField('PK', primary_key=True, db_column='id_employee')
    name = models.CharField('Name', db_column='nm_employee', max_length=100)
    hiring_date = models.DateField('Start date', db_column='dt_hiring')
    seniority = models.IntegerField('Seniority level', db_column='nu_seniority', null=True, blank=True)
    salary = models.FloatField('Salary', db_column='vl_salary')

    department = models.ForeignKey(to=Department, on_delete=models.PROTECT, db_column='id_department')
    role = models.ForeignKey(to=Role, on_delete=models.PROTECT, db_column='id_role')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
