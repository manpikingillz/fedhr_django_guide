# Generated by Django 3.2.13 on 2023-09-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_date_and_expiration_date_and_issued_date_on_visainformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentstatus',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
