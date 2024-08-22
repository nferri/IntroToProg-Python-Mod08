# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_processing_classes.py
# Description: Testing the classes for employee ratings script
# Natalie Ferri, August 19, 2024. Creating test script for Assignment08
# Natalie Ferri, August 21, 2024. Trying to correct the module callable error
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []
        self.temp_file.close()

    def tearDown(self):
        # Clean up and delete the temporary file
        import os
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Smith", "ReviewDate": "2024-08-14", "ReviewRating": 5},
            {"FirstName": "Alice", "LastName": "Wonderland", "ReviewDate": "2024-08-15", "ReviewRating": 4},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_employee_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, Employee.Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 4)

    def test_write_employee_data_to_file(self):
        # Create some sample employee objects
        sample_employees = [
            Employee.Employee(first_name="John", last_name="Smith", review_date="2024-08-14", review_rating=5),
            Employee.Employee(first_name="Alice", last_name="Wonderland", review_date="2024-08-15", review_rating=4),
        ]

        # Call the write_employee_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["ReviewRating"], 4)

if __name__ == "__main__":
    unittest.main()
