# Generated by Django 3.2.13 on 2022-12-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_add_username_field_to_baseuser_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
