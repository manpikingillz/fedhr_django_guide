# Generated by Django 3.2.13 on 2023-09-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employmentstatus_effective_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinformation',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
