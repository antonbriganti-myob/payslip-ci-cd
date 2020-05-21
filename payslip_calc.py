from tax_bracket import TaxBracket


class PayslipCalculator:
    def create_payslip(self, employee_name, annual_salary, super_rate):
        gross_income = self.calculate_gross_income(annual_salary)
        income_tax = self.calculate_income_tax(annual_salary)
        net_income = self.calculate_net_income(gross_income, income_tax)
        super_earned = self.calculate_super_earned(gross_income, super_rate)

        payslip = 'Name: {} \nGross Income: {}\nIncome Tax: {}\nNet income: {}\nSuper Earned: {}'

        return payslip.format(employee_name, gross_income, income_tax, net_income, super_earned)

    def calculate_income_tax(self, annual_salary):
        tax_brackets = [(0, 18200, 0, 0),
                        (18201, 37000, 0.19, 0),
                        (37001, 87000, 0.325, 3572),
                        (87001, 180000, 0.37, 19822),
                        (18001, float("inf"), 0.45, 54232)]

        for bracket in tax_brackets:
            if annual_salary <= bracket[1]:
                return round((bracket[3] + (annual_salary - bracket[0]) * bracket[3]) / 12)

    def calculate_gross_income(self, annual_salary):
        return round(annual_salary / 12)

    def calculate_net_income(self, gross_income, income_tax):
        return gross_income - income_tax

    def calculate_super_earned(self, gross_income, super_rate):
        return round(gross_income * super_rate)



