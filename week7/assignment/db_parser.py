from bs4 import BeautifulSoup
from classes.database_access import DB_Connect
import pymysql
import os.path
import csv
import json
import unicodedata

my_db = DB_Connect('root','','python_projects')

try:
    my_db.executeQuery("SELECT * FROM customer_data")
except:
    my_db.executeQuery("CREATE TABLE customer_data (customer_ID INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30), street VARCHAR(50), city VARCHAR(30), state CHAR(5), zip VARCHAR(5))")
    my_db.conn.commit()
    my_db.executeQuery("CREATE TABLE tmp_customer_data (customer_ID INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30), street VARCHAR(50), city VARCHAR(30), state CHAR(5), zip VARCHAR(5))")
    my_db.conn.commit()
    my_db.executeQuery("CREATE TABLE customer_data_working (customer_ID INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30), street VARCHAR(50), city VARCHAR(30), state CHAR(5), zip VARCHAR(5))")
    my_db.conn.commit()

file_name_incorrect = False
while not file_name_incorrect:
    initial_question = input("What is the filename of the file you would like to import to the database? Type it exactly as it is named! If you don't want to import a file type quit. ")

    file_extens = initial_question.split(".")

    file_extension_string = repr(file_extens[-1])
    if file_extension_string == "\'xml\'":
        if os.path.isfile("text_files/" + initial_question):
            my_file = open("text_files/" + initial_question, encoding="utf-8")
            my_text = my_file.read()
            my_xml = BeautifulSoup(my_text, "xml")
            my_crm_data = my_xml.find_all("entry")
            my_db.executeQuery("TRUNCATE TABLE customer_data_working")
            for entry in my_crm_data:
                my_db.executeQuery("INSERT INTO customer_data_working (first_name,last_name,street,city,state,zip) VALUES (\""+ str(entry.first_name.get_text()) + "\",\""+ str(entry.last_name.get_text()) + "\",\""+ str(entry.street.get_text()) + "\",\""+ str(entry.city.get_text()) + "\",\"" + str(entry.state.get_text()) + "\",\"" + str(entry.zip.get_text())+"\");")
                my_db.conn.commit()
        else:
            file_name_incorrect = True
            print("You did not enter a valid file name! Closing program... ")
    elif file_extension_string == "\'csv\'":
        if os.path.isfile("text_files/" + initial_question):
            my_db.executeQuery("TRUNCATE TABLE customer_data_working")
            with open("text_files/" + initial_question, encoding="utf-8") as csvfile:
                csv_data = csv.reader(csvfile)
                next(csv_data)
                for row in csv_data:
                    insert_data_statement = ('INSERT INTO customer_data_working (first_name,last_name,street,city,state,zip) VALUES (\"' + str(row[0]) + " \",\"" + str(row[1]) + "\" ,\" " + str(row[2]) + "\",\"" + str(row[3]) + " \",\"" + str(row[4]) + "\",\"" + str(row[5]) + "\");")
                    my_db.executeQuery(insert_data_statement)
                my_db.conn.commit()
        else:
            file_name_incorrect = True
            print("You did not enter a valid file name! Closing program... ")
    elif file_extension_string == "\'json\'":
        if os.path.isfile("text_files/" + initial_question):
            my_db.executeQuery("TRUNCATE TABLE customer_data_working")
            sqlstatement = ''
            with open("text_files/" + initial_question, encoding="utf-8") as jsonfile:
                jsondata = json.loads(jsonfile.read())
            for json in jsondata:
                keylist = "("
                valuelist = "("
                firstPair = True
                for key, value in json.items():
                    if not firstPair:
                        keylist += ","
                        valuelist += ","
                    firstPair = False
                    keylist += key
                    if type(value) in (str, unicodedata):
                        valuelist += '"' + value + '"'
                    else:
                        valuelist += str(value)
                keylist += ")"
                valuelist += ")"
                sqlstatement += "INSERT INTO customer_data_working " + keylist + " VALUES " + valuelist + "\n"
            sqlstatement = sqlstatement.splitlines()
            for statement in sqlstatement:
                my_db.executeQuery(statement)
                my_db.conn.commit()
        else:
            file_name_incorrect = True
            print("You did not enter a valid file name! Closing program... ")
    elif initial_question == "quit":
        my_db.executeQuery("START TRANSACTION")
        my_db.executeQuery("RENAME TABLE python_projects.customer_data_working TO python_projects.tmp_customer_data, python_projects.customer_data TO python_projects.customer_data_working, python_projects.tmp_customer_data TO python_projects.customer_data;")
        my_db.executeQuery("COMMIT")
        exit()
    else:
        print("You did not enter a valid entry. Closing program...")
        exit()

