import json

import mysql.connector

from database_query import my_db, my_cursor, Database


class CreateTextFileDep(dict):
    Database.dbQueries()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


try:
    my_dict = CreateTextFileDep()
    select_department = """SELECT * FROM com_details"""
    my_db.cursor()
    my_cursor.execute(select_department)
    result = my_cursor.fetchall()

    for row in result:
        my_dict.add(row[0],
                    ({"HR_Name": row[1], "Acc_Manager_Name": row[2], "Pro_Manager_Name": row[3], "Lead_Name": row[4]}))

    dep_text = json.dumps(my_dict, indent=4, sort_keys=True)
    with open('dep.txt', 'w') as outfile:
        json.dump(my_dict, outfile, indent=4, sort_keys=True)

except mysql.connector.Error as error:
    print("Failed to load text file due to database empty {}".format(error))


class CreateTextFileEmp(dict):
    Database.dbQueries()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


try:
    my_dict = CreateTextFileEmp()
    select_department = """SELECT * FROM emp_details"""
    my_db.cursor()
    my_cursor.execute(select_department)
    result = my_cursor.fetchall()

    for row in result:
        my_dict.add(row[0],
                    ({"Emp_Name": row[1], "Emp_Email": row[2], "Emp_Phone_No": row[3], "Emp_Address": row[4]}))

    emp_text = json.dumps(my_dict, indent=4, sort_keys=True)
    with open('emp.txt', 'w') as outfile:
        json.dump(my_dict, outfile, indent=4, sort_keys=True)

except mysql.connector.Error as error:
    print("Failed to load text file due to database empty {}".format(error))
