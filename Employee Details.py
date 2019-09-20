import os
def enter_choice():
    print('---------------------Enter choise----------------------')
    print("1.create a file\n2.view the file\n3.Append the file\n4.Delete the file.\n0 To Exit")
    num=int(input("Enter your choice:"))
    if num==1:
        create_file()
    elif num==2:
        view_file()
    elif num==3:
        append_file()
    elif num==4:
        empdelete() 
    elif num==0:
        print("---------------------Thank you-------------------")
    else:
        print("------------error try again---------------------")
        enter_choice()
def create_file():
    print('---------------------Employee Info----------------------')
    emp_id=input("Enter employee ID\n")
    name=input("Enter the employee name:\n")
    desg=input("Enter Employee Designation:\n")
    salary=input("Enter Employee salary:\n")
    with open(emp_id,'w')as output_file:
        output_file.write("ID:"+emp_id+"\nName:"+name+"\nDesignation:"+desg+"\nSalary:"+salary)
    print("Employee",emp_id,"is created")
    enter_choice()

def view_file():
    print('---------------------Employee Info----------------------')
    emp_id=input("Enter Employee ID:")
    with open(emp_id,'r')as open_file:
        contents=open_file.read()
        print(contents)
        open_file.close()
    enter_choice()

def append_file():
    print('---------------------Append Employee Info----------------------')
    emp_id=input("Enter employee ID\n")
    name=input("Enter the employee name:\n")
    desg=input("Enter Employee Designation:\n")
    salary=input("Enter Employee salary:\n")
    with open(emp_id,'a')as output_file:
        output_file.write("ID:"+emp_id+"\nName:"+name+"\nDesignation:"+desg+"\nSalary:"+salary)
    print("Employee",emp_id,"is appended")
    enter_choice()
def empdelete():
    filename=input("Entwer Employee ID to delete:")
    if os.path.exists(filename):
        os.remove(filename)
        print("Report",filename,"deleted")
    else:
        print("sorry,I can not find %s report."%filename)       
    enter_choice()
enter_choice()    
