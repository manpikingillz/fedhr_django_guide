import factory
from fedhr.files.models import File
from fedhr.users.tests.factories import BaseUserFactory


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = File
    file = factory.django.FileField(filename='the_file.pdf')
    original_file_name = factory.Faker('file_name')
    file_name = factory.Faker('file_name')
    file_type = factory.Faker('file_name')
    uploaded_by = factory.SubFactory(BaseUserFactory)
    upload_finished_at = factory.Faker('date_time_this_decade')
