import factory
from fedhr.files.tests.factories import FileFactory
from fedhr.setup.models import Country
from fedhr.employee.models import Employee


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    country_name = factory.Faker('country')


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
    nationality = factory.SubFactory(CountryFactory)
    avatar = factory.SubFactory(FileFactory)

    # Job Information
    hire_date = factory.Faker('date_between', start_date='-1y', end_date='today')

    # Identification Information
    social_security_number = factory.Faker('ssn')
    national_identification_number = factory.Faker('ssn')
    tax_identification_number = factory.Faker('ssn')

    email = factory.Faker('email')
    home_email = factory.Faker('email')
    mobile_number = factory.Faker('phone_number')
    work_phone = factory.Faker('phone_number')
    home_phone = factory.Faker('phone_number')

    # Address Information
    street1 = factory.Faker('street_address')
    street2 = factory.Faker('secondary_address')
    city = factory.Faker('city')
    province = factory.Faker('state')
    country = factory.SubFactory(CountryFactory)
    zip_code = factory.Faker('postcode')

    # Social Information
    linked_in = factory.Faker('uri')
    facebook = factory.Faker('uri')
    twitter = factory.Faker('uri')
    instagram = factory.Faker('uri')
