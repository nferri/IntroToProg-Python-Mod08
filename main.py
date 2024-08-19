# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Main.py
# Description: A collection of classes for managing the application
# Natalie Ferri, August 18, 2024. Creating Main.py from Assignment08
# ------------------------------------------------------------------------------------------------- #

# Import necessary classes for file processing, user input/output, and employee data management
from processing_classes import FileProcessor
from presentation_classes import IO
from data_classes import Employee

# Constant for the file name where employee data will be stored
FILE_NAME: str = 'EmployeeRatings.json'

# Menu string displayed to the user with options
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

# Initialize an empty list to hold employee data
employees: list = []

# Load existing employee data from the specified file into the 'employees' list
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)

# Main loop to continuously display the menu and process user choices
while True:
    # Display the menu options to the user
    IO.output_menu(menu=MENU)
    
    # Get the user's menu choice
    menu_choice = IO.input_menu_choice()

    # Handle the menu choice
    if menu_choice == "1":  # Option to display current employee data
        try:
            # Output the employee data to the user
            IO.output_employee_data(employee_data=employees)

        except Exception as e:
            # Output an error message if an exception occurs
            IO.output_error_messages(e)

        continue  # Return to the beginning of the loop for the next menu option

    elif menu_choice == "2":  # Option to enter new employee data
        try:
            # Get new employee data from the user and update the 'employees' list
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            # Display the updated employee data
            IO.output_employee_data(employee_data=employees)

        except Exception as e:
            # Output an error message if an exception occurs
            IO.output_error_messages(e)

        continue  # Return to the beginning of the loop for the next menu option

    elif menu_choice == "3":  # Option to save employee data to a file
        try:
            # Save the current employee data to the specified file
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            # Notify the user that the data was saved successfully
            print(f"Data was saved to the {FILE_NAME} file.")

        except Exception as e:
            # Output an error message if an exception occurs
            IO.output_error_messages(e)

        continue  # Return to the beginning of the loop for the next menu option

    elif menu_choice == "4":  # Option to exit the program
        break  # Exit the while loop and end the program
