# pattern_drawing.py

# Prompt the user to input a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to track the current row
current_row = 0

# Use a while loop to iterate through each row
while current_row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    # Print a new line after each row
    print()
    # Move to the next row
    current_row += 1
