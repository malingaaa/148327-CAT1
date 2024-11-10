class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Displays the employee's details."""
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        """Updates the employee's salary."""
        self.salary = new_salary
        print(f"Salary for {self.name} updated to ${self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  

    def add_employee(self, employee):
        """Adds an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        """Calculates and returns the total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: ${total_salary}")
        return total_salary

    def display_all_employees(self):
        """Displays all employees in the department."""
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()

def main():
    # Initializing department
    department = Department(department_name="Engineering")

    while True:
        print("\nOptions:")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees")
        print("4. Display total salary expenditure")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Add a new employee
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
            except ValueError:
                print("Invalid salary input. Please enter a numeric value.")
                continue
            
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            # Update an employee's salary
            employee_id = input("Enter employee ID to update salary: ")
            employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)
            if employee:
                try:
                    new_salary = float(input(f"Enter new salary for {employee.name}: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid salary input. Please enter a numeric value.")
            else:
                print("Employee not found.")

        elif choice == "3":
            # Display all employees
            department.display_all_employees()

        elif choice == "4":
            # Display total salary expenditure
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            # Quit the program
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

# Run the interactive program
main()
