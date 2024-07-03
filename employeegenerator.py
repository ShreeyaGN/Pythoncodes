# already Created a dictionary of employees with nested dictionaries here generator and decorator used
employees = {
    'Shreeya': {'emp_number': 123, 'designation': 'python'},
    'Muthu': {'emp_number': 456, 'designation': 'python'},
    'priya': {'emp_number': 789, 'designation': 'java'},
    'pooja': {'emp_number': 101, 'designation': 'python'},
    'Ravi': {'emp_number': 102, 'designation': 'java'}
}


# Generator for employees with designation 'j'
def designation_j():
    for key, val in employees.items():
        if val['designation'] == 'java':
            yield key

# Generator for employees with designation 'p'
def designation_p():
    for key, val in employees.items():
        if val['designation'] == 'python':
            yield key

# Create lists using the generators
list_java = list(designation_j())
list_python = list(designation_p())

print("Employees with designation 'java'-", list_java)
print("Employees with designation 'python'-", list_python)

#now using decorator , print all the available information of the employees
def header():
    print("---------------------------------------------------------------")
    
def footer():
    print()
    print("---------------------------------------------------------------")
    
def emp_header():
    print("employee\t\temployee_number\t\t\tdesignation")
    
def emp_info():
     for key, val in employees.items():
         if(val['designation']=="python"):
            print(f"{key}\t\t\t\t{val['emp_number']}\t\t\t{val['designation']}")
def emp_info_java():
     for key, val in employees.items():
         if(val['designation']=="java"):
            print(f"{key}\t\t\t\t{val['emp_number']}\t\t\t{val['designation']}")
 
    
header()
emp_header()
header()
emp_info()
footer()
emp_info_java()
footer()
    
    
