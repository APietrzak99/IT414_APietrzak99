import re

def findAllDates(passed_string):
    dateRegex = re.compile(r'\b(\d)(\d){0,1}\b(-|/)\b(\d)(\d){0,1}\b(-|/)\b(\d\d\d\d)\b')
    dateList = dateRegex.findall(passed_string)
    date_return_list = []

    for date in dateList:
        temp_date = ""
        for item in date:
            temp_date = temp_date + str(item)
        date_return_list.append(temp_date)
        
    return date_return_list

def isValidDate(passed_date):
    dateRegex = re.compile(r'(\d){1,2}(-|/)(\d){1,2}(-|/)\d\d\d\d')
    dateTest = dateRegex.search(passed_date)
    if dateTest is None:
        print("You did not enter a proper date. ")
        return False
    else:
        if passed_date == dateTest.group():
            print("You entered a proper date. ")
            return True
        else:
            print("You did not enter a proper date. ")
            return False