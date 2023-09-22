class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        print("Position: Manager")

class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")
        print("Position: Developer")

    # Function to add a new employee to the team
def add_employee():
    position = input("Enter employee position (Manager/Developer): ")
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    salary = float(input("Enter employee salary: "))

    if position.lower() == "manager":
        department = input("Enter manager's department: ")
        employee = Manager(name, employee_id, salary, department)
    elif position.lower() == "developer":
        programming_language = input("Enter developer's programming language: ")
        employee = Developer(name, employee_id, salary, programming_language)
    else:
        print("Invalid position entered. Employee not added.")
        return

    employees.append(employee)
    print(f"{position} added successfully!")

    # Function to display all employee details
def display_employees():
    for employee in employees:
        employee.display_details()
        print("\n")

    # Main program
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Display Employee Details")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        if not employees:
            print("No employees to display.")
        else:
            display_employees()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
