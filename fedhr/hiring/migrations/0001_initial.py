# Generated by Django 3.2.13 on 2022-11-11 08:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0002_add_fields_and_models_to_expand_employee_model'),
        ('setup', '0001_initial'),
        ('emails', '0002_email_removed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('application_status_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('street1', models.CharField(blank=True, max_length=255, null=True)),
                ('street2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=50, null=True)),
                ('date_available', models.DateTimeField(blank=True, null=True)),
                ('desired_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='all_uploads')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='all_uploads')),
                ('referred_by', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter_username', models.CharField(blank=True, max_length=50, null=True)),
                ('highest_education', models.CharField(blank=True, max_length=255, null=True)),
                ('college_or_university', models.CharField(blank=True, max_length=255, null=True)),
                ('referrence', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('employment_type_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('application_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_applications', to='hiring.applicationstatus')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='hiring.candidate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('job_title', models.CharField(max_length=255, unique=True)),
                ('job_status', models.CharField(blank=True, choices=[('DRAFT', 'Draft'), ('OPEN', 'Open'), ('ON_HOLD', 'On Hold'), ('FILLED', 'Filled'), ('CANCELLED', 'Cancelled')], max_length=20, null=True)),
                ('minimum_experience', models.CharField(blank=True, choices=[('ENTRY_LEVEL', 'Entry Level'), ('MID_LEVEL', 'Mid Level'), ('EXPERIENCED', 'Experienced'), ('MANAGER', 'Manager'), ('SENIOR_MANAGER', 'Senior Manager'), ('EXECUTIVE', 'Executive'), ('SENIOR_EXECUTIVE', 'Senior Executive')], max_length=50, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('compensation', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setup.country')),
                ('employment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hiring.employmenttype')),
                ('hiring_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_openings', to='employee.department')),
                ('hiring_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_openings', to='employee.employee')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('question_type_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TalentPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('talent_pool_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TalentPoolApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('reason_for_adding_candidate', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiring.candidate')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
                ('talent_pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiring.talentpool')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('question_name', models.CharField(max_length=255, unique=True)),
                ('question_category', models.CharField(choices=[('APPLICATION_QUESTION', 'Application Question'), ('ADDITIONAL_QUESTION', 'Additional Question')], max_length=50)),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_opening_questions', to='hiring.questiontype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobOpeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('is_required', models.BooleanField(default=False)),
                ('job_opening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_opening_questions', to='hiring.jobopening')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_opening_questions', to='hiring.question')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicationQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application_question_answers', to='hiring.candidate')),
                ('job_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application_question_answers', to='hiring.jobapplication')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicationEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.email')),
                ('job_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application_emails', to='hiring.jobapplication')),
                ('sent_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_application_emails', to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplicationComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('removed', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
                ('job_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application_comments', to='hiring.jobapplication')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_application_comment_replies', to='hiring.jobapplicationcomment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_opening',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='hiring.jobopening'),
        ),
        migrations.AddConstraint(
            model_name='jobopeningquestion',
            constraint=models.UniqueConstraint(fields=('job_opening', 'question'), name='unique_job_opening_question'),
        ),
        migrations.AddConstraint(
            model_name='jobapplicationquestionanswer',
            constraint=models.UniqueConstraint(fields=('job_application', 'candidate'), name='unique_job_application_candidate_answer'),
        ),
    ]
