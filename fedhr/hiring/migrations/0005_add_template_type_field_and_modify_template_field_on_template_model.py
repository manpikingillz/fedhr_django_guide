# Generated by Django 3.2.13 on 2023-09-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0004_add_template_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='template',
            new_name='template_content',
        ),
        migrations.AddField(
            model_name='template',
            name='template_type',
            field=models.CharField(blank=True, choices=[('EMAIL_TEMPLATE', 'Email Template'), ('JOB_OFFER_TEMPLATE', 'Job Offer Template'), ('CONTRACT_TEMPLATE', 'Contract Template')], max_length=50, null=True),
        ),
    ]
