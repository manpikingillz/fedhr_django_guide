from django.db import transaction
from fedhr.employee.models import Employee
from django.core.exceptions import ValidationError
from fedhr.common.services import model_update, model_delete
from fedhr.employee.models import Note, Education

EMPLOYEE_INSTANCE_IS_NONE = f'You attempted updating a {Employee.__name__} that does not exist!'
EMPLOYEE_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {Employee.__name__} that does not exist!'
NOTE_INSTANCE_IS_NONE = f'You attempted updating a {Note.__name__} that does not exist!'
NOTE_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {Note.__name__} that does not exist!'
EDUCATION_INSTANCE_IS_NONE = f'You attempted updating a {Education.__name__} that does not exist!'
EDUCATION_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {Education.__name__} that does not exist!'


# Employee =====================================================
def employee_create(
    *,
    first_name,
    last_name,
    **extra_fields
) -> Employee:
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        **extra_fields
    )

    employee.full_clean()
    employee.save()

    return employee


@transaction.atomic
def employee_update(*, employee: Employee, data) -> Employee:
    if not data:
        raise ValidationError('No data updates were provided.')
    model_fields = list(vars(employee).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not employee:
        raise ValidationError(EMPLOYEE_INSTANCE_IS_NONE)

    _employee, has_updated = model_update(
        instance=employee,
        fields=model_fields,
        data=data
    )

    return _employee


@transaction.atomic
def employee_delete(*, employee: Employee):

    if not employee:
        raise ValidationError(EMPLOYEE_INSTANCE_IS_NONE_DELETE)

    model_delete(instance=employee)


# Notes =====================================================
def note_create(
    *,
    note,
    **extra_fields
) -> Note:
    note = Note(
        note=note,
        **extra_fields
    )

    note.full_clean()
    note.save()

    return note


@transaction.atomic
def note_update(*, note: Note, data) -> Note:
    if not data:
        raise ValidationError('No data updates were provided.')
    model_fields = list(vars(note).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not note:
        raise ValidationError(EMPLOYEE_INSTANCE_IS_NONE)

    _note, has_updated = model_update(
        instance=note,
        fields=model_fields,
        data=data
    )

    return _note


@transaction.atomic
def note_delete(*, note: Note):

    if not note:
        raise ValidationError(NOTE_INSTANCE_IS_NONE_DELETE)

    model_delete(instance=note)


# Education =====================================================
def education_create(
    *,
    employee,
    **extra_fields
) -> Education:
    education = Education(
        employee=employee,
        **extra_fields
    )

    education.full_clean()
    education.save()

    return education


@transaction.atomic
def education_update(*, education: Education, data) -> Education:
    if not data:
        raise ValidationError('No data updates were provided.')
    model_fields = list(vars(education).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not education:
        raise ValidationError(EDUCATION_INSTANCE_IS_NONE)

    _education, has_updated = model_update(
        instance=education,
        fields=model_fields,
        data=data
    )

    return _education


@transaction.atomic
def education_delete(*, education: Education):

    if not education:
        raise ValidationError(EDUCATION_INSTANCE_IS_NONE_DELETE)

    model_delete(instance=education)
