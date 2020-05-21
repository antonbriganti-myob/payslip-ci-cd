import unittest
from payslip_calc import PayslipCalculator


class TestPayslipCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = PayslipCalculator()

    def test_calculate_gross_income_correctly_calculates_gross_income(self):
        expected_gross_income = 5004
        actual_gross_income = self.calculator.calculate_gross_income(60050)

        self.assertEqual(expected_gross_income, actual_gross_income)

    def test_calculate_net_income_correctly_calculates_net_income(self):
        expected_net_income = 4082
        actual_net_income = self.calculator.calculate_net_income(5004, 922)

        self.assertEqual(expected_net_income, actual_net_income)

    def test_calculate_super_earned_correctly_calculates_super_earned(self):
        expected_super = 450
        actual_super = self.calculator.calculate_super_earned(5004, 0.09)

        self.assertEqual(expected_super, actual_super)

    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
