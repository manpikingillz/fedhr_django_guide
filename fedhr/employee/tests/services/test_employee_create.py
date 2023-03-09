from django.test import TestCase, Client
from django.urls import reverse
from fedhr.employee.tests.factories import EmployeeFactory
from contextlib import contextmanager

@contextmanager
def TestStep(message: str):
    yield


class EmployeeCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client

    def test_employee_create_flow(self):
        # with TestStep('1. User is authenticated'):

        with TestStep('2. Create mployee with all correct information'):
            data = {
                'first_name': 'Gilbert',
                'last_name': 'Twesigomwe'
            }

            url = reverse('employee_create')
            print('url: ', url)
            response = self.client.post('api/employees', data)
            print(response)
            print('hello were in')
            self.assertTrue(True)

        # with TestStep('3. Missing required fields.'):
        #     ...

        # with TestStep('4. Invalid data on fields.'):
        #     ...

