import platform
import os.path
import shutil
#import functions for essential processes

def copyFolder():
#performs the process of copying over the folder to a new location
    my_path = getPath()
    os.chdir(my_path)
#establishes that the path used is C:/file_explore/

#first input asks user for the name of the folder they want to copy over. folder_dir checks the path established with the user input
    folder_to_copy_from = input("What is the name of the folder you would like to copy? ")
    folder_dir = os.path.join(my_path, folder_to_copy_from)

    if not os.path.exists(folder_to_copy_from):
        #catches if file the user is trying to copy from is invalid
        print("You did not enter a valid folder to copy from. ")
    else:
        #if file they will copy from is valid, then the program will ask for the folder they'd like to copy to, and creates folder_to_dir for joining my_path, and the user_input
        folder_to_copy_to = input("What is the name of the folder you would like the file to be copied to? ")
        folder_to_dir = os.path.join(my_path, folder_to_copy_to)
#checks if user specified folder to copy to exists. if not create the folder then log it in log.txt
        if not os.path.exists(os.path.join(my_path, folder_to_copy_to)):
            os.makedirs(os.path.join(my_path, folder_to_copy_to))
            if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                newLog.write(str(my_path)+ "\\"+str(folder_to_copy_to) + " was created successfully\n")
            else:
                newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                newLog.write(str(my_path)+"\\"+ str(folder_to_copy_to) + " was created successfully\n")
    #create list of files in folder specified and run for loop to check all of them
            file_list = os.listdir(os.path.join(my_path, folder_to_copy_from))
            for file_item in file_list:
    #checks if item in file_list is actually a file, and not a folder
                if os.path.isfile(os.path.join(folder_dir,file_item)):
    #checks the size of the file. if it is over 1GB, it will catch and not be copied to the new location.
                    temp_file_size = os.path.getsize(os.path.join(folder_dir, file_item))
                    temp_file_divide = temp_file_size / 1073741824
                    if temp_file_divide < 1:
                        #copy the file over to new location specified
                        shutil.copy2(os.path.join(folder_dir, file_item), os.path.join(my_path, folder_to_copy_to))
                        #log what was done to log.txt
                        if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                                newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                                newLog.write(str(file_item) + " was copied successfully to " + str(my_path)+ "\\"+ str(folder_to_copy_to)+ '\n')
                        else:
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                            newLog.write(str(file_item) + " was copied successfully to " + str(my_path)+ "\\"+str(folder_to_copy_to) +'\n')
                    else:
                        #log what was done to log.txt
                        if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                            newLog.write(str(file_item) + " was ignored for being over 1GB\n")
                        else:
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                            newLog.write(str(file_item) + " was ignored for being over 1GB.\n")
                else:
                    #log what was done to log.txt
                    if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                        newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                        newLog.write(str(folder_dir)+ "\\"+str(file_item) + " was ignored for being a folder.\n")
                    else:
                        newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                        newLog.write(str(folder_dir)+"\\"+ str(file_item) + " was ignored for being a folder.\n")
        else:
            file_list = os.listdir(os.path.join(my_path, folder_to_copy_from))
            for file_item in file_list:
                #checks if item in file_list is actually a file, and not a folder
                if os.path.isfile(os.path.join(folder_dir,file_item)):
                    #checks the size of the file. if it is over 1GB, it will catch and not be copied to the new location.
                    temp_file_size = os.path.getsize(os.path.join(folder_dir, file_item))
                    temp_file_divide = temp_file_size / 1073741824
                    if temp_file_divide < 1:
                        #copy the file over to new location specified
                        shutil.copy2(os.path.join(folder_dir, file_item), os.path.join(my_path, folder_to_copy_to))
                        #log what was done to log.txt
                        if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                            newLog.write(str(file_item) + " was copied successfully to " + str(my_path)+ "\\"+str(folder_to_copy_to)+ '\n')
                        else:
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                            newLog.write(str(file_item) + " was copied successfully to " + str(my_path)+"\\"+ str(folder_to_copy_to) +'\n')
                    else:
                        #log what was done to log.txt
                        if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                                newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                                newLog.write(str(file_item) + " was ignored for being over 1GB\n")
                        else:
                            newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                            newLog.write(str(file_item) + " was ignored for being over 1GB.\n")
                else:
                    #log what was done to log.txt
                    if os.path.isfile(os.path.join(folder_dir, 'log.txt')):
                        newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'w')
                        newLog.write(str(folder_dir)+"\\"+ str(file_item) + " was ignored for being a folder.\n")
                    else:
                        newLog = open(os.path.join(folder_to_dir, 'log.txt'), 'a')
                        newLog.write(str(folder_dir)+"\\"+ str(file_item) + " was ignored for being a folder.\n")

def drawmenu():

    print("What would you like to do? ")
    print("To copy a folder, enter 'C' ")

def getPath():
    my_system = platform.system()

    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs, "file_explore")

    return final_filepath