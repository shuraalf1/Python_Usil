class Employee:
    """
    Employee Class
    """

    SALARY_BASE = 930

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.sales = []

    def set_sales(self, sales):
        """
        Set sales of employee
        :param sales: list of sales
        :return: None
        """
        self.sales = sales

    def get_sales(self):
        """
        Get sales of employee
        :return: list of sales
        """
        return self.sales

    def get_sum_sales(self):
        """
        Get sum the sales of the employees
        :return: sum of sales
        """
        return sum(self.sales)

    def get_info(self):
        """
        Get information of the employee
        :return: Full name of the employee
        """
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        """
        Get salary of the employee
        :return: Salary
        """

        return self.SALARY_BASE
