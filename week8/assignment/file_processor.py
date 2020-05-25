from classes.database_access import DB_Connect
import pymysql
import os.path
import csv
from filesystem_functions import *

create_table()
file_downloader()
multithread_processor()