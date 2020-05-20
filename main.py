from payslip_calc import PayslipCalculator

employee_name = "John Smith"
annual_salary = 60050
super_rate = 0.09

calc = PayslipCalculator()
payslip = calc.create_payslip(employee_name, annual_salary, super_rate)
print(payslip)
