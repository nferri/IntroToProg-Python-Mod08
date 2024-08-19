# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-processing_classes.py
# Description: A collection of classes for managing the application
# Natalie Ferri, Aug 18, 2024, Creating processing module from Assignment08.py
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.
    ChangeLog:
        Natalie Ferri, 8/18/2024, Created class FileProcessor
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """
        Reads data from a JSON file and loads it into a list of Employee objects.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def read_employee_data_from_file
        
        Parameters:
            file_name (str): The name of the file to read from.
            employee_data (list): The list where Employee objects will be appended.
            employee_type (Employee): The Employee class used to create new Employee objects.
        
        Returns:
            list: The updated list of Employee objects.
        """
        try:
            # Open the specified file in read mode
            with open(file_name, "r") as file:
                
                # Load the JSON data from the file
                list_of_dictionary_data = json.load(file)
                
                # Iterate over each dictionary in the list
                for employee in list_of_dictionary_data:
                    
                    # Create a new Employee object
                    employee_object = employee_type()
                    
                    # Populate the Employee object with data from the JSON dictionary
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    
                    # Add the Employee object to the employee_data list
                    employee_data.append(employee_object)
                    
        except FileNotFoundError:
            # Raise an error if the file is not found
            raise FileNotFoundError("Text file must exist before running this script!")

        except Exception:       
            # Raise a generic error for any other exceptions
            raise Exception("There was a non-specific error!")

        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes data to a JSON file from a list of Employee objects.

        ChangeLog:
            Natalie Ferri, 8/18/2024, Created def write_employee_data_from_file
        
        Parameters:
            file_name (str): The name of the file to write to.
            employee_data (list): The list of Employee objects to write to the file.
        
        Raises:
            TypeError: If there is an issue with data formatting.
            PermissionError: If there is an issue with file permissions.
            Exception: For any other errors encountered.
        """
        try:
            # Create a list to hold dictionaries representing each Employee
            list_of_dictionary_data = []
            
            # Iterate over each Employee object in the list
            for employee in employee_data:

                # Create a dictionary for the Employee object
                employee_json = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }

                # Add the dictionary to the list
                list_of_dictionary_data.append(employee_json)

            # Open the specified file in write mode
            with open(file_name, "w") as file:

                # Write the JSON data to the file
                json.dump(list_of_dictionary_data, file)

        except TypeError:
            # Raise an error if the data is not in a valid JSON format
            raise TypeError("Please check that the data is a valid JSON format")

        except PermissionError:
            # Raise an error if there are permission issues with the file
            raise PermissionError("Please check the data file's read/write permission")

        except Exception as e:
            # Raise a generic error for any other exceptions
            raise Exception("There was a non-specific error!")
