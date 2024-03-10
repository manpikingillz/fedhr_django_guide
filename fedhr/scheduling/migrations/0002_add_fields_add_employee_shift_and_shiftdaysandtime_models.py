# Generated by Django 3.2.13 on 2022-11-13 19:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_add_fields_and_models_to_expand_employee_model'),
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('effective_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_shifts', to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('shift_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShiftDaysAndTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('days', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), blank=True, null=True, size=7)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.shift')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='WorkShift',
        ),
        migrations.AddField(
            model_name='employeeshift',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_shifts', to='scheduling.shift'),
        ),
    ]
