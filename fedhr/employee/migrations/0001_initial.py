# Generated by Django 3.2.13 on 2022-08-05 23:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='employee.division')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='employee.station')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='division',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='employee.region'),
        ),
    ]
