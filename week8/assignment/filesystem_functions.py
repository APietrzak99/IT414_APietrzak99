import csv
import pymysql
from classes.database_access import DB_Connect
import os.path
import ezsheets
import threading
import requests
import openpyxl
import webbrowser
import time
import datetime
from openpyxl import Workbook

def create_table():
    my_db = DB_Connect('root','','python_projects')
    #create grade_data table if it doesn't already exist
    try:
        my_db.executeQuery("SELECT * FROM grade_data")
    except:
        my_db.executeQuery("CREATE TABLE grade_data (grade_ID INT AUTO_INCREMENT PRIMARY KEY, level_of_education VARCHAR(30), test_preparation VARCHAR(20), math_score VARCHAR(5), reading_score VARCHAR(5), writing_score VARCHAR(5))")
        my_db.conn.commit()    

def file_downloader():
    url = 'https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week08/WI20-Assignment/exam_data.csv'
    r = requests.get(url, allow_redirects=True)

    open('text_files/exam_data.csv', 'wb').write(r.content)

def db_processor():
    #db commit area
    my_db = DB_Connect('root','','python_projects')
    if os.path.isfile("text_files/exam_data.csv"):
        #clear all data in my_db
        my_db.executeQuery("TRUNCATE TABLE grade_data")
        with open("text_files/exam_data.csv", encoding="utf-8") as csvfile:
            csv_data = csv.reader(csvfile)
            #skip first row
            next(csv_data)
            #insert all data in the database
            for row in csv_data:
                insert_data_statement = ('INSERT INTO grade_data (level_of_education,test_preparation,math_score,reading_score,writing_score) VALUES (\"' + str(row[0]) + " \",\"" + str(row[1]) + "\" ,\" " + str(row[2]) + "\",\"" + str(row[3]) + " \",\"" + str(row[4]) + "\");")
                my_db.executeQuery(insert_data_statement)
            my_db.conn.commit()
        #takes current date and time
        time_now = datetime.datetime.now()
        #open log in text_files, and writes to it in the format listed
        log_open = open("text_files/script_log.txt", "a")
        log_open.write(time_now.strftime("%b %d %Y %H:%M:%S")+ " - Database Import Processing is Complete! \n")
        log_open.close()

def excel_processor():
        #excel sheet area
        grade_book = Workbook()
        active_sheet = grade_book.active
        #open csv file and read data, which is then added to excel sheet
        with open("text_files/exam_data.csv") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            for row in csv_data:
                active_sheet.append(row)
        grade_book.save("text_files/grade_data.xlsx")
        #take current date and time
        time_now = datetime.datetime.now()
        #open log in text_files, and writes to it in the format listed
        log_open = open("text_files/script_log.txt", "a")
        log_open.write(time_now.strftime("%b %d %Y %H:%M:%S")+ " - Excel Sheet Processing is Complete! \n")
        log_open.close()

def google_sheets_processor():
        #google sheets area
        my_spreadsheet = ezsheets.createSpreadsheet("Grade Data")
        my_url = my_spreadsheet.url
        #set current google sheet and set getrows
        curr_sheet = my_spreadsheet[0]
        rows = curr_sheet.getRows()
        
        #set headers in google sheet
        rows[0][0] = "Parental Level of Education"
        rows[0][1] = "Test Preparation"
        rows[0][2] = "Math Score"
        rows[0][3] = "Reading Score"
        rows[0][4] = "Writing Score"

        row_count_goog = 0
        #csv file is opened and read, data is then added to the rows variable
        with open("text_files/exam_data.csv") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            next(csv_data)
            for data in csv_data:
                rows[row_count_goog][0] = data[0]
                rows[row_count_goog][1] = data[1]
                rows[row_count_goog][2] = data[2]
                rows[row_count_goog][3] = data[3]
                rows[row_count_goog][4] = data[4]
                row_count_goog = row_count_goog + 1          

        #send rows to sheet
        curr_sheet.updateRows(rows)
        webbrowser.open(my_url)
        #take current date and time
        time_now = datetime.datetime.now()
        #open log in text_files, and writes to it in the format listed
        log_open = open("text_files/script_log.txt", "a")
        log_open.write(time_now.strftime("%b %d %Y %H:%M:%S")+ " - Google Sheet Processing is Complete! \n")
        log_open.close()


def multithread_processor():
    thread1 = threading.Thread(target=excel_processor)
    thread1.start()

    thread2 = threading.Thread(target=google_sheets_processor)
    thread2.start()

    thread3 = threading.Thread(target=db_processor)
    thread3.start()