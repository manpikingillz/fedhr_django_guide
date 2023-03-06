from django.test import TestCase
from fedhr.employee.tests.factories import EmployeeFactory
from contextlib import contextmanager

@contextmanager
def TestStep(message: str):
    yield


class EmployeeCreateTestCase(TestCase):
    def test_employee_create_flow(self):
        with TestStep('1. User is authenticated'):
            employee = EmployeeFactory.build()
            print(employee.__dict__)
            print('hello were in')
            self.assertTrue(True)

        # with TestStep('2. Create mployee with all correct information'):
        #     pass

        # with TestStep('3. Missing required fields.'):
        #     ...

        # with TestStep('4. Invalid data on fields.'):
        #     ...
