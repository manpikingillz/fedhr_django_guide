# Generated by Django 3.2.13 on 2023-01-30 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_add_firstname_lastname_to_baseuser_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='username',
        ),
    ]
