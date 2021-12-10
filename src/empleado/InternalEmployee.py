from .Employee import Employee


class InternalEmployee(Employee):
    """
    Internal employee class
    """

    SALES_COMMISSION = 0.60

    def get_salary(self):
        """
        Get salary of internal employee
        :return: Calculated salary
        """
        return self.SALARY_BASE + (self.get_sum_sales() * self.SALES_COMMISSION)
