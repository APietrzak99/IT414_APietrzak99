from twilio.rest import Client
import psutil
import smtplib
import datetime 
import time
import json

time_now = datetime.datetime.now()

cpu_resource_values = []
ram_resource_values = []
drive_resource_values = []
network_resource_values = []

def cpu_usage(accountID,authToken,trialNumber,cellNumber):
    overall_cpu = psutil.cpu_percent(interval=.1)
    cpu_resource_values.append(overall_cpu)
    cpu_cores = psutil.cpu_percent(interval=.1, percpu=True)
    cpu_resource_values.append(cpu_cores)
    if overall_cpu > 85:
        func_call = last_text(time_now)
        if func_call == True:
            twClient = Client(accountID, authToken)
            my_message = twClient.messages.create(body=time_now.strftime("%b %d %Y %H:%M:%S")+  " - The total CPU used on your computer is at" + str(overall_cpu) + "%" +  " Please address immediately", from_=trialNumber, to=cellNumber)

def disk_usage(accountID,authToken,trialNumber,cellNumber):
    volumes = psutil.disk_partitions()
    for volume in volumes:
        drive_resource_values.append(volume[1])
        drive_resource_values.append(psutil.disk_usage(volume[1]))
        for item in psutil.disk_usage(volume[1]):
            if item < 100 and item > 90:
                func_call = last_text(time_now)
                if func_call == True:
                    twClient = Client(accountID, authToken)
                    my_message = twClient.messages.create(body="\n" + time_now.strftime("%b %d %Y %H:%M:%S")+  " - The " + volume[1] + " volume on your computer is " + str(item) + "%" +  " full and is almost out of space.\nPlease address immediately.", from_=trialNumber, to=cellNumber)
                else:
                    pass

def network_packets(accountID,authToken,trialNumber,cellNumber):
    network = psutil.net_io_counters()
    network_resource_values.append(network[0])
    network_resource_values.append(network[1])
    network_resource_values.append(network[4])
    network_resource_values.append(network[5])
    network_resource_values.append(network[6])
    network_resource_values.append(network[7])
    if network[4] != 0 or network[5] !=0:
        func_call = last_text(time_now)
        if func_call == True:
            twClient = Client(accountID, authToken)
            my_message = twClient.messages.create(body=time_now.strftime("%b %d %Y %H:%M:%S")+  " - Network statistics are currently showing " + network[4] + " errors in, and " + network[5] + " errors out. Please address immediately", from_=trialNumber, to=cellNumber)
    if network[6] != 0 or network[7] != 0:
        func_call = last_text(time_now)
        if func_call == True:
            twClient = Client(accountID, authToken)
            my_message = twClient.messages.create(body=time_now.strftime("%b %d %Y %H:%M:%S")+  " - Network statistics are currently showing " + network[6] + " dropped packets in, and " + network[7] + " dropped packets out. Please address immediately", from_=trialNumber, to=cellNumber)

def ram_usage(accountID,authToken,trialNumber,cellNumber):
    ram = psutil.virtual_memory()
    ram_resource_values.append(ram[2])
    ram_resource_values.append(ram[3])
    ram_resource_values.append(ram[4])
    if ram[2] > 90:
        func_call = last_text(time_now)
        if func_call == True:
            twClient = Client(accountID, authToken)
            my_message = twClient.messages.create(body=time_now.strftime("%b %d %Y %H:%M:%S")+  " - The RAM used on your computer is at" + str(ram[2]) + "%" +  " Please address immediately", from_=trialNumber, to=cellNumber)

def last_text(time_of_text):
    #read json data
    with open("text_files/script_config.json", "rb") as config:
        reading = config.read()
        data = json.loads(reading)
    #convert json data to list format
    json_list = []
    for item in data:
        json_list.append(item)
#this list will only contain all the values within the json file
    temp_list = []
    for item in json_list:
        for key,value in item.items():
            temp_list.append(value)
    #this will check if the list with all the keys appended to it is equal to 11, i.e. if the last_text key has been added to script_config.json
    if len(temp_list) == 11:
        time_in_list = temp_list[10]
        converted_time_in_list = datetime.datetime.strptime(time_in_list, "%Y-%m-%d %H:%M:%S.%f")
        #the function will return True if the time the function is called is more than an hour after the time that is in the json file
        #first piece will compare the hours in the datetimes, the second statement is for if it is a new day
        if time_of_text.hour-converted_time_in_list.hour > 0 or time_of_text.day-converted_time_in_list.day > 0:
            #write new time the text has been ran if the time between the last sent text and now is greater than an hour to json file
            json_list[0]["last_text"] = str(time_of_text)

            with open("text_files/script_config.json", "w") as config:
                json.dump(json_list, config)
            return True
        else:
            return False
    else:
        #create last_text key in json file
        json_list[0]["last_text"] = str(time_of_text)

        with open("text_files/script_config.json", "w") as config:
            json.dump(json_list, config)
        return True


# with open("text_files/script_config.json", "rb") as config:
#     reading = config.read()
#     data = json.loads(reading)
# values_list = []

# for item in data:
#     for key, value in item.items():
#         values_list.append(value)
# print(cpu_resource_values)
# print(drive_resource_values)
# print(ram_resource_values)
# print(network_resource_values)
# smtpConn = smtplib.SMTP(values_list[0], values_list[1])
# smtpConn.ehlo()
# smtpConn.starttls()

# smtpConn.login(values_list[2], values_list[3])
# Date = time.ctime(time.time())
# Subject = "Server Status"
# Text = "The computer's usage statistics are as follows:\n""" + drive_resource_values[0] + " drive is " + "%  "+ "full\n" + str(cpu_resource_values[0]) + "% " + "overall CPU used\n" + str(cpu_resource_values[1]) + " Each number in this list represent the percentage of a CPU core being used.\n" + str(ram_resource_values[0]) + "% " + " total RAM used\n" + str(ram_resource_values[1]) + " total RAM available in bytes\n" + str(ram_resource_values[2]) + " total RAM used in bytes\n" + str(network_resource_values[0]) + " bytes being sent and "+ str(network_resource_values[1]) + " bytes being received by the network.\n" + str(network_resource_values[2]) + "errors in and " + str(network_resource_values[3]) + " errors out.\n" + str(network_resource_values[4]) + " packets dropped in and " +  str(network_resource_values[5]) + " packets dropped out.\n"
# #Format mail message
# my_message = ('\nDate:             %s\nSubject: %s\n%s\n' %
#             (Date, Subject, Text))

# smtpConn.sendmail(values_list[4], values_list[5], my_message)

# smtpConn.close()