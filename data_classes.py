# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-data_classes.py
# Description: A collection of classes for managing the application
# Natalie Ferri, August 18, 2024. Creating data_classes.py from Assignment08
# ------------------------------------------------------------------------------------------------- #

from datetime import date

class Person:
    """
    A class representing person data.

    ChangeLog:
        Natalie Ferri, 8/18/2024, Created Person class.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a Person instance with optional first and last names.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def __init__

        Parameters:
            first_name (str): The person's first name (default is an empty string).
            last_name (str): The person's last name (default is an empty string).
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first name of the person with proper title casing.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def first_name

        Returns:
            str: The person's first name in title case.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the first name of the person. Validates that it contains only alphabetic characters or is empty.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def first name setter

        Parameters:
            value (str): The first name to set.
        
        Raises:
            ValueError: If the value contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        Gets the last name of the person with proper title casing.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def last_name
      
        Returns:
            str: The person's last name in title case.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the last name of the person. Validates that it contains only alphabetic characters or is empty.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def last name setter
       
        Parameters:
            value (str): The last name to set.
        
        Raises:
            ValueError: If the value contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        Returns a string representation of the person with their first and last names.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def __str__
        
        Returns:
            str: The full name of the person.
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data, inheriting from Person.

    ChangeLog:
        Natalie Ferri, 8/18/2024, Created Employee class.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The date of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5).
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        """
        Initializes an Employee instance with optional first and last names, review date, and rating.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created __init__ function.
        
        Parameters:
            first_name (str): The employee's first name (default is an empty string).
            last_name (str): The employee's last name (default is an empty string).
            review_date (str): The date of the employee's review in YYYY-MM-DD format (default is "1900-01-01").
            review_rating (int): The employee's review rating (default is 3).
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Gets the review date of the employee.
        
        ChangeLog:
            Natalie Ferri, 8/18/2024, Created review_date function.
       
        Returns:
            str: The review date in YYYY-MM-DD format.
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Sets the review date of the employee. Validates that the date is in the correct format.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created review_date setter.
      
        Parameters:
            value (str): The review date to set in YYYY-MM-DD format.
        
        Raises:
            ValueError: If the date is not in the correct format.
        """
        try:
            date.fromisoformat(value)  # Validate the date format
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Gets the review rating of the employee.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created review_rating function.
        
        Returns:
            int: The review rating (1-5).
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """
        Sets the review rating of the employee. Validates that the rating is between 1 and 5.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created review_rating setter.

        Parameters:
            value (int): The review rating to set.
        
        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        Returns a string representation of the employee with their first name, last name, review date, and review rating.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def __str__
        
        Returns:
            str: The employee's details in a formatted string.
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.review_rating}"
