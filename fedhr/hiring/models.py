from django.db import models
from fedhr.common.models import BaseModel
from fedhr.emails.models import Email
from fedhr.employee.models import Employee, Department, Location
from fedhr.setup.models import Country


class EmploymentType(BaseModel):
    '''
        Possible values:
            - Contracter, Full-Time, Intern, Part-Time
    '''
    employment_type_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.employment_type_name


# Create your models here.
class JobOpening(BaseModel):
    class JobStatus(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        OPEN = 'OPEN', 'Open'
        ON_HOLD = 'ON_HOLD', 'On Hold'
        FILLED = 'FILLED', 'Filled'
        CANCELLED = 'CANCELLED', 'Cancelled'

    class Experience(models.TextChoices):
        ENTRY_LEVEL = 'ENTRY_LEVEL', 'Entry Level'
        MID_LEVEL = 'MID_LEVEL', 'Mid Level'
        EXPERIENCED = 'EXPERIENCED', 'Experienced'
        MANAGER = 'MANAGER', 'Manager'
        SENIOR_MANAGER = 'SENIOR_MANAGER', 'Senior Manager'
        EXECUTIVE = 'EXECUTIVE', 'Executive'
        SENIOR_EXECUTIVE = 'SENIOR_EXECUTIVE', 'Senior Executive'

    job_title = models.CharField(max_length=255, unique=True)
    job_status = models.CharField(
        choices=JobStatus.choices, max_length=20,
        null=True, blank=True)
    hiring_lead = models.ForeignKey(
        Employee, on_delete=models.SET_NULL,
        related_name="job_openings", null=True, blank=True)
    hiring_department = models.ForeignKey(
        Department, on_delete=models.SET_NULL,
        related_name="job_openings", null=True, blank=True)
    employment_type = models.ForeignKey(
        EmploymentType, on_delete=models.SET_NULL,
        null=True, blank=True)
    minimum_experience = models.CharField(
        choices=Experience.choices,
        max_length=50, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL,
        null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL,
        null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    compensation = models.DecimalField(
        max_digits=12, decimal_places=2,
        null=True, blank=True)


class QuestionType(BaseModel):
    '''
        Possible Values:
            - Short Answer, Long Answer, Yes/No,
            - Multiple Choice, Checkbox, File Upload
    '''
    question_type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.question_type_name


class Question(BaseModel):
    class QuestionCategory(models.TextChoices):
        '''
            Aplication Questions examples:
            - Resume, Address, LinkedIn URL, Date Available,
              Desired Salary, Cover Letter, Reffered By, Website/Blog/Portfolio, Twitter Username,
              Highest Education, College/University, Refferences

            Additional Question Examples:
            - How did you hear about this position?
            - What skills can you bring to this role?
            - Who reffered you for this position?
            - How did you hear about us?
            - What's your biggest strength?
            - Why do you want to work here?
        '''
        APPLICATION_QUESTION = 'APPLICATION_QUESTION', 'Application Question'
        ADDITIONAL_QUESTION = 'ADDITIONAL_QUESTION', 'Additional Question'

    question_name = models.CharField(max_length=255, unique=True)
    question_type = models.ForeignKey(
        QuestionType, on_delete=models.CASCADE,
        related_name='job_opening_questions')
    question_category = models.CharField(
        choices=QuestionCategory.choices, max_length=50)


class JobOpeningQuestion(BaseModel):
    job_opening = models.ForeignKey(
        JobOpening, on_delete=models.CASCADE,
        related_name='job_opening_questions')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='job_opening_questions')
    is_required = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['job_opening', 'question'],
                name='unique_job_opening_question'
            )
        ]


class Candidate(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        null=True, blank=True)
    date_available = models.DateTimeField(null=True, blank=True)
    desired_salary = models.DecimalField(
        max_digits=12, decimal_places=2,
        null=True, blank=True)
    resume = models.FileField(
        upload_to='all_uploads', blank=True, null=True)
    cover_letter = models.FileField(
        upload_to='all_uploads', blank=True, null=True)
    referred_by = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    twitter_username = models.CharField(max_length=50, null=True, blank=True)
    highest_education = models.CharField(
        max_length=255, null=True, blank=True)
    college_or_university = models.CharField(
        max_length=255, null=True, blank=True)
    referrence = models.CharField(max_length=255, null=True, blank=True)


class ApplicationStatus(BaseModel):
    '''
        Possible Values:
            - New, Reviewed, Schedule Phone Screen, Phone Screened, Schedule Interview,
              Interviewed, Put on Hold, Checking referrences, Offer Sent, Hired
    '''
    application_status_name = models.CharField(max_length=255)


class JobApplication(BaseModel):
    job_opening = models.ForeignKey(
        JobOpening,
        on_delete=models.CASCADE,
        related_name='job_applications')
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='job_applications')
    application_status = models.ForeignKey(
        ApplicationStatus,
        related_name='job_applications',
        on_delete=models.SET_NULL, null=True, blank=True)


class JobApplicationQuestionAnswer(BaseModel):
    job_application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='job_application_question_answers')
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='job_application_question_answers')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['job_application', 'candidate'],
                name='unique_job_application_candidate_answer')
        ]


class JobApplicationComment(BaseModel):
    job_application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='job_application_comments')
    comment = models.TextField()
    created_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True, blank=True)
    reply_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='job_application_comment_replies',
        null=True, blank=True)


class JobApplicationEmail(BaseModel):
    job_application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='job_application_emails')
    sent_from = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name='job_application_emails',
        null=True, blank=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)


class TalentPool(BaseModel):
    talent_pool_name = models.CharField(max_length=255)
    description = models.TextField()


class TalentPoolApplicant(BaseModel):
    talent_pool = models.ForeignKey(TalentPool, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True, blank=True)
    reason_for_adding_candidate = models.TextField()
