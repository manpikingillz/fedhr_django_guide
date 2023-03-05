import factory
from fedhr.utils.tests import faker

from fedhr.employee.models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    preferred_name = factory.Faker('first_name')
    gender = factory.Faker('random_element', elements=('MALE', 'FEMALE'))
    date_of_birth = factory.Faker('date_of_birth', minimum_age=18, maximum_age=50)
    marital_status = factory.Faker('random_element', elements=('SINGLE', 'MARRIED', 'COMMON_LAW', 'DOMESTIC_PARTNERSHIP'))
    nationality = factory.Faker('country')
    avatar = factory.Faker('image_url', width=None, height=None)

    # Job Information
    hire_date = factory.Faker('date_between', start_date='-1y', end_date='today')

    # Identification Information
    social_security_number = factory.Faker('ssn')
    national_identification_number = factory.Faker('ssn')
    tax_identification_number = factory.Faker('ssn')

    # Address Information
    street1 = factory.Faker('street_address')
    street2 = factory.Faker('secondary_address')
    city = factory.Faker('city')
    province = factory.Faker('state')
    country = factory.Faker('country')
    zip_code = factory.Faker('postcode')

    # Social Information
    linked_in = factory.Faker('uri')
    facebook = factory.Faker('uri')
    twitter = factory.Faker('uri')
    instagram = factory.Faker('uri')
