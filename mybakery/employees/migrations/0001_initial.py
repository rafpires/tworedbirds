# Generated by Django 3.2.9 on 2021-11-24 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(db_column='id_department', primary_key=True, serialize=False, verbose_name='PK')),
                ('name', models.CharField(db_column='nm_department', max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(db_column='id_role', primary_key=True, serialize=False, verbose_name='PK')),
                ('name', models.CharField(db_column='nm_role', max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(db_column='id_employee', primary_key=True, serialize=False, verbose_name='PK')),
                ('name', models.CharField(db_column='nm_employee', max_length=100, verbose_name='Name')),
                ('hiring_date', models.DateField(db_column='dt_hiring', verbose_name='Start date')),
                ('seniority', models.IntegerField(blank=True, db_column='nu_seniority', null=True, verbose_name='Seniority level')),
                ('salary', models.FloatField(db_column='vl_salary', verbose_name='Salary')),
                ('department', models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.PROTECT, to='employees.department')),
                ('role', models.ForeignKey(db_column='id_role', on_delete=django.db.models.deletion.PROTECT, to='employees.role')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
            },
        ),
    ]
