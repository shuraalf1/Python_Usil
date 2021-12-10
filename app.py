from src.empleado.Employee import Employee
from src.empleado.ExternalEmployee import ExternalEmployee
from src.empleado.InternalEmployee import InternalEmployee

normal_employee = Employee('Pedro', 'Arias')
external_employee = ExternalEmployee('Luis', 'Aguirre')
internal_employee = InternalEmployee('Mary', 'Musk')

normal_employee.set_sales([100, 80, 20])
external_employee.set_sales([100, 80, 20])
internal_employee.set_sales([100, 80, 20])

print(normal_employee.get_info())
print(normal_employee.get_salary())

print(external_employee.get_info())
print(external_employee.get_salary())

print(internal_employee.get_info())
print(internal_employee.get_salary())
