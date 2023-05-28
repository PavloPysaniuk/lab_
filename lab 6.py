import math

def calculate_e(a, m, b):
    """Calculate the expected value for a task."""
    return (a + 4 * m + b) / 6

def calculate_sd(a, b):
    """Calculate the standard deviation for a task."""
    return (b - a) / 6

def calculate_ci(tasks):
    """Calculate the confidence interval for the project."""
    # Calculate the expected value and standard deviation for each task
    e_values = []
    sd_values = []
    for task in tasks:
        e_values.append(calculate_e(*task))
        sd_values.append(calculate_sd(task[0], task[2]))

    # Calculate the expected value and standard deviation for the project
    e_project = sum(e_values)
    sd_project = math.sqrt(sum([sd ** 2 for sd in sd_values]))

    # Calculate the confidence interval for the project
    ci_min = e_project - 2 * sd_project
    ci_max = e_project + 2 * sd_project

    return ci_min, ci_max

# Prompt the user to enter task estimates
tasks = []
while True:
    a = float(input("Enter the 'a' estimate for a task: "))
    m = float(input("Enter the 'm' estimate for a task: "))
    b = float(input("Enter the 'b' estimate for a task: "))
    tasks.append((a, m, b))

    # Ask the user if they want to enter another task
    another_task = input("Do you want to enter another task? (y/n) ")
    if another_task.lower() != "y":
        break

# Calculate the confidence interval for the project
ci_min, ci_max = calculate_ci(tasks)

# Print the result
print(f"Project's 95% confidence interval: {ci_min:.2f} ... {ci_max:.2f} points")
