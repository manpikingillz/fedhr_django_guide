import factory

from fedhr.users.models import BaseUser


class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseUser

    email = factory.Faker('email')
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = factory.Faker('boolean')
    is_admin = factory.Faker('boolean')
    jwt_key = factory.Faker('sha1')
