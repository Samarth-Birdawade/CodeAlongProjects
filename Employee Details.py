n = int(input("Enter number of employees: "))

employees = {}

for i in range(1, n+1):
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Employee Salary: "))
    employees[i] = {"name": emp_name, "salary": emp_salary}

while True:
    search_id = int(input("Enter Employee ID to search: "))
    if search_id not in range(1, n+1):
        print("Employee ID not found.")
        break
    else:
        print(f"| Employee Details |\n\tEmployee Found: ID: {search_id} \n\tName: {employees[search_id]['name']} \n\tSalary: {employees[search_id]['salary']}")
        continue