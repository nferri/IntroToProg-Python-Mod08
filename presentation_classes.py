# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-presentation_classes.py
# Description: A collection of classes for managing the application
# Natalie Ferri, August 18, 2024. Creating presentation_classes.py from Assignment08
# ------------------------------------------------------------------------------------------------- #

# Import the Employee class from data_classes module
from data_classes import Employee

class IO:
    """
    A collection of presentation layer functions that manage user input and output.
    ChangeLog:
        Natalie Ferri, 8/18/2024, Created class IO
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message to the user.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def output_error_message     
        
        Parameters:
            message (str): The custom error message to display.
            error (Exception, optional): The exception to provide additional details.
        """
        print(message, end="\n\n")
        if error is not None:

            # Display detailed technical error information if available
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu of choices to the user.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def output_menu
            
        Parameters:
            menu (str): The menu string to display.
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Gets a menu choice from the user and validates it.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def input_menu_choice
       
        Returns:
            str: The validated menu choice entered by the user.
        """
        choice = "0"
        try:
            # Prompt the user to enter a menu choice
            choice = input("Enter your menu choice number: ")

            # Validate the menu choice
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")

        except Exception as e:
            # Display an error message if the input is invalid
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays employee data to the user in a formatted manner.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def output_employee_data
            
        Parameters:
            employee_data (list): A list of Employee objects to display.
        """
        print()
        print("-" * 50)

        # Iterate through the employee data and display each employee's information
        for employee in employee_data:

            # Determine the rating message based on the review rating
            if employee.review_rating == 5:
                message = "{} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = "{} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = "{} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = "{} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = "{} {} is rated as 1 (Not Meeting Expectations)"
            
            # Display the employee's name, review date, and rating
            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))

        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """
        Gets new employee data from the user and adds it to the employee data list.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def input_employee_data

        Parameters:
            employee_data (list): The current list of Employee objects.
            employee_type (Employee): The Employee class used to create new employee objects.
        
        Returns:
            list: The updated list of Employee objects.
        """
        try:
            # Create a new Employee object
            employee_object = employee_type()

            # Collect employee details from the user
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))

            # Append the new employee object to the employee_data list
            employee_data.append(employee_object)

        except ValueError as e:
            # Display an error message if there is a data type mismatch
            IO.output_error_messages("That value is not the correct type of data!", e)

        except Exception as e:
            # Display a generic error message for any other exceptions
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
