# Generated by Django 3.2.13 on 2023-09-16 06:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_add_relationship_model_change_relationship_field_emergency_contact_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('asset_category_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True)),
                ('date_assigned', models.DateField(blank=True, null=True)),
                ('date_returned', models.DateField(blank=True, null=True)),
                ('asset_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.assetcategory')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
