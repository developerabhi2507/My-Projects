import mysql.connector


class Database:
    def __init__(self, my_database, my_connect):
        self.my_database = my_database
        self.my_connect = my_connect

    @staticmethod
    def dbQueries():
        # Create table ------------------------------------------------------------
        database = "Company_db"
        SQL = "CREATE DATABASE IF NOT EXISTS " + database + ";"
        my_cursor.execute(SQL)
        my_db.commit()

        SQL = "USE " + database + ";"
        my_cursor.execute(SQL)

    @staticmethod
    def companyTableForm():
        # Create table ---------------------------------------------------------
        Tables = {"com_details": (
                "CREATE TABLE IF NOT EXISTS " + "com_details" + "("
                                                                "    Uni_ID INT AUTO_INCREMENT PRIMARY KEY, "
                                                                "    HR_Name VARCHAR(50), "
                                                                "    Acc_Manager_Name VARCHAR(50), "
                                                                "    Pro_Manager_Name VARCHAR(50), "
                                                                "    Lead_Name VARCHAR(50)"
                                                                ");"
        )}

        # Create company data ---------------------------------------------------------
        my_cursor.execute(Tables["com_details"])
        my_db.commit()

    @staticmethod
    def employeeTableForm():
        # Create table ---------------------------------------------------------
        Tables = {"emp_details": (
                "CREATE TABLE IF NOT EXISTS " + "emp_details" + "("
                                                                "    Emp_ID INT AUTO_INCREMENT PRIMARY KEY, "
                                                                "    Emp_Name VARCHAR(40), "
                                                                "    Emp_Email VARCHAR(40), "
                                                                "    Emp_Phone_No INT(10), "
                                                                "    Emp_Address VARCHAR(40)"
                                                                ");"
        )}
        # Create employee data -----------------------------------------------
        my_cursor.execute(Tables["emp_details"])
        my_db.commit()


# Connect to DB -----------------------------------------------------------
my_db = mysql.connector.connect(host="localhost", user="root", password="password")
my_cursor = my_db.cursor()
db = Database(my_db, my_cursor)
