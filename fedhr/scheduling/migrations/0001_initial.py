# Generated by Django 3.2.13 on 2022-11-13 19:05

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0002_add_fields_and_models_to_expand_employee_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('work_shift_name', models.CharField(max_length=255, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('days', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), blank=True, null=True, size=7)),
                ('has_end_date', models.BooleanField(default=False)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('employees', models.ManyToManyField(related_name='work_shifts', to='employee.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
