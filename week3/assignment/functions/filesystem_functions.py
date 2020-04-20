import platform
import os.path
import shutil
import send2trash
import re
from zipfile import ZipFile
import zipfile

def deleteFile():
    my_path = getPath()
    temp_file = ""
    fileNameRegex = re.compile(r'([a-z_]*\.com)')
    access_logs_path = os.path.join(my_path,"access_logs")

    with open(os.path.join(my_path,'matches.txt'),'r') as text:
        for line in text:
            temp_file = temp_file + line
    
    for line in temp_file:
        fileName = fileNameRegex.findall(temp_file)

    for root, dirs, files in os.walk(access_logs_path):
        for file in files:
            if file not in fileName:
                send2trash.send2trash(os.path.join(root,file))
                send2trash.send2trash(root)

def final_zip():
    my_path = getPath()
    zip = zipfile.ZipFile("text_files\\results.zip", "w")

    for root, subdirs, files in os.walk(my_path):
        zip.write(root)
        for file in files:
            zip.write(os.path.join(root,file))

def getRoot():
    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs)

    return final_filepath

def getCopyPath():
    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs, "log_processing")

    return final_filepath

def getPath():
    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs, "logs")

    return final_filepath

def moveFile():
    my_path = getPath()
    my_root = getRoot()

    file_to_move = input("What is the name of the file you would like to move? ")
    folder_to_move_to = input("What is the name of the folder you would like the file to be moved to? ")

    shutil.move(os.path.join(my_path,file_to_move), os.path.join(my_root,folder_to_move_to))

def readLogs():

    temp_data_set = ""
    filtered_IP_list = []
    filtered_file_list = []

    my_path = getPath()

    access_logs_path = os.path.join(my_path,"access_logs")

    for root, subdirs, files in os.walk(access_logs_path):
        for file in files:
            with open(os.path.join(root,file),'r') as logFile:
                for line in logFile:
                    fileFound = re.search(r'(\.)(\.)(/)', line)
                    if fileFound:
                        temp_data_set = temp_data_set + line
                        temp_data_set = temp_data_set + " Filename: " + str(file) + "\n"
                    wpFound = re.search(r'(/)(wp-login)(\.)(php)(\?)(action=register)', line)
                    if wpFound:
                        temp_data_set = temp_data_set + line
                        temp_data_set = temp_data_set + " Filename: " + str(file) + "\n"
                    HTTPFound = re.search(r'\b(\d)(\d)(\d)?(\d)?(\d)?( )(403)\b', line)
                    if HTTPFound:
                        temp_data_set = temp_data_set + line
                        temp_data_set = temp_data_set + " Filename: " + str(file) + "\n"
                    selectFound = re.search(r'(select)', line)
                    if selectFound:
                        temp_data_set = temp_data_set + line
                        temp_data_set = temp_data_set + " Filename: " + str(file) + "\n"
                    installFound = re.search(r'(install)', line)
                    if installFound:
                        temp_data_set = temp_data_set + line
                        temp_data_set = temp_data_set + " Filename: " + str(file) + "\n"

    IPRegex = re.compile(r'\b(\d)(\d)?(\d)?(\.)(\d)(\d)?(\d)?(\.)(\d)(\d)?(\d)?(\.)(\d)(\d)?(\d)?\b')
    fileNameRegex = re.compile(r'([^"]\B [a-z_]*\.com)')
    IPList = IPRegex.findall(temp_data_set)
    fileList = fileNameRegex.findall(temp_data_set)
    for IP in IPList:
        temp_IP = ""
        for item in IP:
            temp_IP = temp_IP + str(item.lstrip())
        if temp_IP not in filtered_IP_list:
            filtered_IP_list.append(temp_IP)
    for fileName in fileList:
        temp_file = ""
        for item in fileName:
            temp_file = temp_file + str(item.lstrip())
        if temp_file not in filtered_file_list:
            filtered_file_list.append(temp_file)

    final_info = dict(zip(filtered_IP_list, filtered_file_list))
    with open(os.path.join(my_path,'matches.txt'), 'w') as file:
        for key in final_info.items():
            file.write("%s,%s\n" % key)
            
def renameFile():
    my_path = getPath()
    my_return = os.walk(os.path.join(my_path,"access_logs"))

    for item in my_return:
        for filename in item[2]:
            temp_filename = "processed_" + filename
            shutil.move(os.path.join(item[0], filename), os.path.join(item[0], temp_filename))
    
def unzipFile():
    my_root = getRoot()
    
    os.chdir('week3\\assignment')

    if os.path.isdir(os.path.join(my_root, "logs")):
        with ZipFile('text_files\\access_logs.zip', 'r') as zipObj:
            zipObj.extractall(os.path.join(my_root, 'logs'))
    else:
        os.makedirs(os.path.join(my_root, 'logs'))
        with ZipFile('text_files\\access_logs.zip', 'r') as zipObj:
            zipObj.extractall(os.path.join(my_root, 'logs'))
    