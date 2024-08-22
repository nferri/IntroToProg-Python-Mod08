# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_processing_classes.py
# Description: Testing the classes for employee ratings script
# Natalie Ferri, August 19, 2024. Creating test script for Assignment08
# Natalie Ferri, August 21, 2024. Trying to correct the module callable error
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Smith','2024-08-15', '5']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Smith')
            self.assertEqual(self.employee_data[0].review_date, '2024-08-15')
            self.assertEqual(self.employee_data[0].review_rating, 5)

        # Simulate invalid review input (not a float)
        with patch('builtins.input', side_effect=['Alice', 'Wonderland', 'invalid']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()
  
 
