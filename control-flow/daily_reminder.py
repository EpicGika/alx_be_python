# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level entered."

# Modify reminder if the task is time-bound
if priority in ["high", "medium", "low"]:
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."

# Output the reminder
print(f"Reminder: {reminder}")
