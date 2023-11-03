class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id  # Instance variable for employee ID
        self.emp_name = emp_name  # Instance variable for employee name
        self.emp_salary = emp_salary  # Instance variable for employee salary

    def display_employee_details(self):
        # Accessing instance variables within the class method
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)

# Creating an Employee instance
employee1 = Employee(1, "John Doe", 50000)

# Accessing instance variables from outside the class
print("Accessing instance variables outside the class:")
print("Employee ID:", employee1.emp_id)
print("Employee Name:", employee1.emp_name)
print("Employee Salary:", employee1.emp_salary)

# Accessing instance variables using the display_employee_details method
print("\nAccessing instance variables using the display_employee_details method:")
employee1.display_employee_details()
