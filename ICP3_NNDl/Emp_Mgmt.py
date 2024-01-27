class Employee:
    # Class variable to count the number of employees
    emp_count = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # Increment the employee count when a new employee is created
        Employee.emp_count += 1

    def display_employee_details(self):
        print(f"Name: {self.name}, Family: {self.family}, Salary: {self.salary}, Department: {self.department}")

    @staticmethod
    def avg_salary(employee_list):
        total_salary = sum(employee.salary for employee in employee_list)
        return total_salary / len(employee_list) if len(employee_list) > 0 else 0


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        # Call the constructor of the base class (Employee)
        super().__init__(name, family, salary, department)

    def display_employee_details(self):
        super().display_employee_details()


# Creating instances of Employee class
emp1 = Employee("Hari", "Ram", 50000, "Admin")
emp2 = Employee("Krishna", "Ram", 60000, "Fullstack")

# Creating instances of FulltimeEmployee class
fulltime_emp1 = FulltimeEmployee("Fulltime Raj", "Krishna Doe Family", 80000, "IT")
fulltime_emp2 = FulltimeEmployee("Fulltime Ravi", "kumar Family", 90000, "Ln App")

# Displaying employee details
print("Employee Details:")
emp1.display_employee_details()
emp2.display_employee_details()

print("\nFulltime Employee Details:")
fulltime_emp1.display_employee_details()
fulltime_emp2.display_employee_details()

# Displaying the average salary of all employees
all_employees = [emp1, emp2, fulltime_emp1, fulltime_emp2]
avg_salary = Employee.avg_salary(all_employees)
print(f"\nAverage Salary of all employees: {avg_salary}")
