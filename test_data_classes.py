# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_data_classes.py
# Description: Testing the classes for employee ratings script
# Natalie Ferri, August 19, 2024, Creating test script for Assignment08
# ------------------------------------------------------------------------------------------------- #

import unittest
from datetime import date
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    """
    Test cases for the Person class from data_classes module.
    Natalie Ferri, August 19. 2024. Created class. 
    """

    def test_person_init(self):
        """
        Test the initialization of Person with valid first and last names.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        person = Person("John", "Smith")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Smith")

    def test_person_default_init(self):
        """
        Test the initialization of Person with default values.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        person = Person()
        self.assertEqual(person.first_name, "")
        self.assertEqual(person.last_name, "")

    def test_person_invalid_first_name(self):
        """
        Test that Person initialization raises a ValueError for invalid first names.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        with self.assertRaises(ValueError):
            person = Person("John1", "Smith")  # Invalid first name with digit
        with self.assertRaises(ValueError):
            person = Person("John", "Smith1")  # Invalid last name with digit

    def test_person_str(self):
        """
        Test the string representation of Person.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        person = Person("John", "Smith")
        self.assertEqual(str(person), "John,Smith")

class TestEmployee(unittest.TestCase):
    """
    Test cases for the Employee class from data_classes module.
    Natalie Ferri, August 19. 2024. Created class. 
    """

    def test_employee_init(self):
        """
        Test the initialization of Employee with valid parameters.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        employee = Employee("Alice", "Wonderland", "2024-08-18", 4)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Wonderland")
        self.assertEqual(employee.review_date, "2024-08-18")
        self.assertEqual(employee.review_rating, 4)

    def test_employee_default_init(self):
        """
        Test the initialization of Employee with default values.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        employee = Employee()
        self.assertEqual(employee.first_name, "")
        self.assertEqual(employee.last_name, "")
        self.assertEqual(employee.review_date, "1900-01-01")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_invalid_review_date(self):
        """
        Test that Employee initialization raises a ValueError for invalid review dates.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Barker", "2024-08-32", 4)  # Invalid date
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Barker", "2024-02-30", 4)  # Invalid date

    def test_employee_invalid_review_rating(self):
        """
        Test that Employee initialization raises a ValueError for invalid review ratings.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2024-08-18", 0)  # Rating below minimum
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2024-08-18", 6)  # Rating above maximum
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2024-08-18", "invalid_rating")  # Non-integer rating

    def test_employee_str(self):
        """
        Test the string representation of Employee.
        Natalie Ferri, August 19. 2024. Created class. 
        """
        employee = Employee("Eve", "Brown", "2024-08-18", 4)
        self.assertEqual(str(employee), "Eve,Brown,2024-08-18,4")

if __name__ == '__main__':
    unittest.main()
