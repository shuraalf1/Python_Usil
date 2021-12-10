from behave import *
from src.empleado.Employee import Employee


@given('an employee')
def step_impl(context):
    context.employee = Employee('Rob', 'Musk')


@when('I set list sales')
def step_impl(context):
    context.employee.set_sales([20, 30])


@then('I get the salary must be greater than or equal to $930')
def step_impl(context):
    assert context.employee.get_salary() >= 930
