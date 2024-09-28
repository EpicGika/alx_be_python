# explore_datetime.py

import datetime
from datetime import timedelta  # Import timedelta to calculate future dates

# Part 1: Display the Current Date and Time


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date


def calculate_future_date():
    # Prompt the user to enter the number of days
    number_of_days = int(input("Enter the number of days to add to the current date"))

    # Get the current date
    current_date = datetime.datetime.now()

    # Calculate the future date
    future_date = current_date + timedelta(days=number_of_days)

    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print("Future Date:", formatted_future_date)


# Call the functions
display_current_datetime()
calculate_future_date()
