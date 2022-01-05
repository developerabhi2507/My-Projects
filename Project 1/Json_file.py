import json

import mysql.connector

from database_query import my_db, my_cursor, Database


class CreateJsonDep(dict):
    Database.dbQueries()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


try:
    my_dict = CreateJsonDep()
    select_department = """SELECT * FROM com_details"""
    my_db.cursor()
    my_cursor.execute(select_department)
    result = my_cursor.fetchall()

    for row in result:
        my_dict.add(row[0],
                    ({"HR_Name": row[1], "Acc_Manager_Name": row[2], "Pro_Manager_Name": row[3], "Lead_Name": row[4]}))

    dep_json = json.dumps(my_dict, indent=4, sort_keys=True)
    with open('dep.json', 'w') as outfile:
        json.dump(my_dict, outfile, indent=4, sort_keys=True)

    for i in my_dict:
        print(
            f"{i} {my_dict[i]['Acc_Manager_Name']} {my_dict[i]['HR_Name']} {my_dict[i]['Lead_Name']} {my_dict[i]['Pro_Manager_Name']}")

    # print(dep_json)

except mysql.connector.Error as error:
    print("Failed to print json file due to database empty {}".format(error))


class CreateJsonEmp(dict):
    Database.dbQueries()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


try:
    my_dict = CreateJsonEmp()
    select_department = """SELECT * FROM emp_details"""
    my_db.cursor()
    my_cursor.execute(select_department)
    result = my_cursor.fetchall()

    for row in result:
        my_dict.add(row[0],
                    ({"Emp_Name": row[1], "Emp_Email": row[2], "Emp_Phone_No": row[3], "Emp_Address": row[4]}))

    emp_json = json.dumps(my_dict, indent=4, sort_keys=True)
    with open('emp.json', 'w') as outfile:
        json.dump(my_dict, outfile, indent=4, sort_keys=True)

    for i in my_dict:
        print(
            f"{i} {my_dict[i]['Emp_Name']} {my_dict[i]['Emp_Email']} {my_dict[i]['Emp_Phone_No']} "
            f"{my_dict[i]['Emp_Address']}")

    # print(emp_json)

except mysql.connector.Error as error:
    print("Failed to print json file due to database empty {}".format(error))
