from .Employee import Employee


class ExternalEmployee(Employee):
    """
    External employee class
    """

    SALES_COMMISSION = 0.10

    def get_salary(self):
        """
        Get salary of external employee
        :return: Calculated salary
        """
        return self.SALARY_BASE + (self.get_sum_sales() * self.SALES_COMMISSION)
