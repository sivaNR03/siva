# Initialize an empty dictionary to store employee data
employee_dict = {}

# Function to add an employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    domain = input("Enter Domain: ")
    email = input("Enter Email: ")

    # Create a dictionary to store the employee's details
    employee_details = {
        "Name": name,
        "Domain": domain,
        "EmpID": emp_id,
        "Email": email
        }

    # Add the employee details to the main dictionary
    employee_dict[emp_id] = employee_details
    print("Employee added successfully!")

# Function to print employee details
def print_employee():
    emp_id = input("Enter Employee ID to print details: ")
    if emp_id in employee_dict:
        employee_details = employee_dict[emp_id]
        print("Employee Details:")
        for key, value in employee_details.items():
            print(f"{key}: {value}")
    else:
        print(f"Employee with ID {emp_id} not found!")

# Main program loop
while True:
    print("\n1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        print_employee()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
