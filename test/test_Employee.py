import pytest
from src.empleado.Employee import Employee


@pytest.fixture
def employee():
    normal_employee = Employee('Rob', 'Musk')
    return normal_employee


def test_get_sales(employee):
    assert employee.get_sales() == []


def test_set_sales(employee):
    list_sales = [20, 30]
    employee.set_sales(list_sales)

    assert employee.get_sales() == list_sales


def test_get_sum_sales(employee):
    list_sales = [20, 30]
    sum_sales = sum(list_sales)
    employee.set_sales(list_sales)

    assert employee.get_sum_sales() == sum_sales


def test_get_info(employee):
    assert employee.get_info() == 'Rob Musk'


def test_get_salary(employee):
    assert employee.get_salary() == employee.SALARY_BASE
