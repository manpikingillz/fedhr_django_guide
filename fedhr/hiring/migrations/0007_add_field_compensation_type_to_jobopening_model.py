# Generated by Django 3.2.13 on 2023-09-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0006_add_fields_to_job_opening_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopening',
            name='compensation_type',
            field=models.CharField(blank=True, choices=[('HOURLY', 'Hourly'), ('MONTHLY', 'Monthly')], max_length=20, null=True),
        ),
    ]
