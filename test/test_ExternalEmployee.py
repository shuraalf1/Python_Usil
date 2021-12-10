import pytest
from src.empleado.ExternalEmployee import ExternalEmployee


@pytest.fixture
def employee():
    external_employee = ExternalEmployee('Rob', 'Musk')
    return external_employee


def test_get_salary(employee):
    list_sales = [20, 30]
    employee.set_sales(list_sales)
    salary_calculated = employee.SALARY_BASE + (sum(list_sales) * employee.SALES_COMMISSION)

    assert employee.get_salary() == salary_calculated
