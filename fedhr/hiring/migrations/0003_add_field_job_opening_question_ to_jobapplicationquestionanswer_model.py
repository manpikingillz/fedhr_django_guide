# Generated by Django 3.2.13 on 2022-11-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0002_add_field_answer_to_jobapplicationquestionanswer_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicationquestionanswer',
            name='job_opening_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_application_question_answers', to='hiring.jobopeningquestion'),
        ),
    ]
