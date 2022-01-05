from Com_details import createCompanySheet, mergeCompanySheet, saveCompanyWorkbook, deleteCompanyData, deleteInSheet
from Emp_details import createEmployeeSheet, saveEmployeeWorkBook, mergeEmployeeSheet
from Json_file import CreateJsonDep, CreateJsonEmp
from Text_file import CreateTextFileDep, CreateTextFileEmp
from database_query import Database

# # Connect to DB -----------------------------------------------------------
# my_db = mysql.connector.connect(host="localhost", user="root", password="password")
# my_cursor = my_db.cursor()

while True:
    user = input(
        "Welcome our Company...!\n"
        "Press 1 for create new excel sheet of company,\n"
        "Press 2 for merge your sheet with existing company sheet\n"
        "Press 3 for create new excel sheet of employee,\n"
        "Press 4 for merge your excel sheet with existing employee sheet\n"
        "Press 5 for delete data\n"
        "Press enter for exit\n"
    )
    if user == "1":
        Database.dbQueries()
        Database.companyTableForm()
        createCompanySheet(
            input("Enter the HR_Name: "),
            input("Enter the Acc_Manager_Name: "),
            input("Enter the Pro_Manager_Name: "),
            input("Enter the Lead_Name: ")
        )
        saveCompanyWorkbook()

    elif user == "2":
        mergeCompanySheet()

    elif user == "3":
        Database.dbQueries()
        Database.employeeTableForm()
        createEmployeeSheet(
            input("Enter the Emp_Name: "),
            input("Enter the Emp_Email: "),
            input("Enter the Emp_Phone_No: "),
            input("Enter the Emp_Address: "),
        )
        saveEmployeeWorkBook()

    elif user == "4":
        mergeEmployeeSheet()

    # elif user == "5":
    #     user = input("Press 1 for department details, Press 2 for employee details\n")
    #     if user == "1":
    #         print(dep_json)
    #     elif user == "2":
    #         print(emp_json)

    elif user == "5":
        deleteCompanyData()
        deleteInSheet()
        CreateJsonDep()
        CreateTextFileDep()
        CreateJsonEmp()
        CreateTextFileEmp()

    elif user == "":
        exit()

    # createCompanySheet(1, "Tom", "Herbie", "Jazz", "Hermon")
    # createCompanySheet(2, "Jordan", "Rohan", "Krishna", "Simon")
