from django.test import TestCase
from django.core.exceptions import ValidationError

from fedhr.users.services import user_create
from fedhr.users.models import BaseUser
from fedhr.users.tests.factories import BaseUserFactory


class UserCreateTests(TestCase):
    def test_user_without_password_is_created_with_unusable_one(self):
        base_user = BaseUserFactory.build()
        print(base_user.__dict__)
        user = user_create(
            email='random_user@domain.io',
            username='johndoe'
        )

        self.assertFalse(user.has_usable_password())

    def test_user_with_capitalized_email_cannot_be_created(self):
        user_create(
            email='random_user@domain.io',
            username='johndoe'
        )

        with self.assertRaises(ValidationError):
            user_create(
                email='RANDOM_user@domain.io',
                username='johndoe'
            )

        self.assertEqual(1, BaseUser.objects.count())
