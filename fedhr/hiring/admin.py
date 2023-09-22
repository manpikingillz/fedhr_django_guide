from django.contrib import admin

from fedhr.hiring.models import (
    ApplicationStatus, Candidate, JobApplication,
    JobApplicationComment, JobApplicationEmail,
    JobApplicationQuestionAnswer, JobOpening,
    JobOpeningQuestion, Question, QuestionType,
    TalentPool, TalentPoolApplicant, Template)


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    fields = (
        'job_title',
        'job_status',
        'hiring_lead',
        'hiring_department',
        'employment_type',
        'minimum_experience',
        'job_description',
        'location',
        'country',
        'city',
        'province',
        'postal_code',
        'compensation',
        'removed'
        )
    list_display = (
        'job_title',
        'job_status',
        'hiring_lead',
        'hiring_department',
        'removed'
        )


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    fields = ('question_type_name', 'removed')
    list_display = ('question_type_name', 'removed')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_name', 'question_type', 'question_category', 'removed')
    list_display = ('question_name', 'question_type', 'question_category', 'removed')


@admin.register(JobOpeningQuestion)
class JobOpeningQuestionAdmin(admin.ModelAdmin):
    fields = ('job_opening', 'question', 'is_required', 'removed')
    list_display = ('job_opening', 'question', 'is_required', 'removed')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 'last_name', 'email', 'phone',
        'street1', 'street2', 'city', 'province', 'zip_code',
        'country', 'date_available', 'desired_salary', 'resume',
        'cover_letter', 'referred_by', 'website', 'twitter_username',
        'highest_education', 'college_or_university', 'referrence', 'removed'
    )

    list_display = ('first_name', 'last_name', 'email', 'phone', 'removed')


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    fields = ('application_status_name', 'removed')
    list_display = ('application_status_name', 'removed')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    fields = ('job_opening', 'candidate', 'application_status')
    list_display = ('job_opening', 'candidate', 'application_status')


@admin.register(JobApplicationQuestionAnswer)
class JobApplicationQuestionAnswerAdmin(admin.ModelAdmin):
    fields = ('job_application', 'job_opening_question',
              'candidate', 'answer', 'removed')
    list_display = ('job_application', 'job_opening_question',
                    'candidate', 'answer', 'removed')


@admin.register(JobApplicationComment)
class JobApplicationCommentAdmin(admin.ModelAdmin):
    fields = ('job_application', 'comment', 'created_by', 'reply_to')
    list_display = ('job_application', 'comment', 'created_by', 'reply_to')


@admin.register(JobApplicationEmail)
class JobApplicationEmailAdmin(admin.ModelAdmin):
    fields = ('job_application', 'sent_from', 'email', 'removed')
    list_display = ('job_application', 'sent_from', 'email', 'removed')


@admin.register(TalentPool)
class TalentPoolAdmin(admin.ModelAdmin):
    fields = ('talent_pool_name', 'description', 'removed')
    list_display = ('talent_pool_name', 'description', 'removed')


@admin.register(TalentPoolApplicant)
class TalentPoolApplicantAdmin(admin.ModelAdmin):
    fields = ('talent_pool', 'candidate', 'created_by', 'reason_for_adding_candidate')
    list_display = ('talent_pool', 'candidate',
                    'created_by', 'reason_for_adding_candidate')


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    fields = ('template_name', 'template_content', 'template_type')
    list_display = ( 'id', 'template_name', 'template_content', 'template_type')
