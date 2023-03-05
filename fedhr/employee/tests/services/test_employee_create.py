from django.test import TestCase
from employee.tests.factories import EmployeeFactory


class EmployeeCreateTestCase(TestCase):
    def test_employee_create(self):
        employee = EmployeeFactory.build()
        print(employee.__dict__)
