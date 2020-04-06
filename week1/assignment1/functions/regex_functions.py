import re

def findAllData(passed_string):
    """searches passed_string and filters data based on regexes listed for CC, coords, and dollar amounts. will then return the list of filtered information
    arguments:
    passed_string
    returns
    full_data_list
    """
    #establish regexes for each column
    coordRegex = re.compile(r'(-)?\b(\d?)(\d?)(\d?)\b(\.|,)\b(\d?)(\d?)(\d?)(\d?)(\d?)\b(, |; )(-)?\b(\d?)(\d?)(\d?)\b(\.|,)\b(\d?)(\d?)(\d?)(\d?)(\d?)\b')
    dollarsRegex = re.compile(r'(\$ )(\d)(,|\.)(\d)(\d)(\d)')
    ccNumRegex = re.compile(r'\b(4)(\d)(\d)(\s?)(\d)(\s?)(\d)(\d)(\s?)(\d)(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}\b')
    #perform findall operations to pull all pieces of data needed
    coordList = coordRegex.findall(passed_string)
    dollarsList = dollarsRegex.findall(passed_string)
    ccNumList = ccNumRegex.findall(passed_string)
    coord_data_list = []
    dollars_data_list = []
    ccNum_data_list = []
    full_data_list = []

    for coord in coordList:
        temp_coord = ""
        for item in coord:
            temp_coord = temp_coord + str(item)
        coord_data_list.append(temp_coord)
    for dollar in dollarsList:
        temp_dollar = ""
        for item in dollar:
            temp_dollar = temp_dollar + str(item)
        dollars_data_list.append(temp_dollar)
    for ccNum in ccNumList:
        temp_CC = ""
        for item in ccNum:
            #filter out non-digit characters, such as \r\n
            if item.isdigit():
                temp_CC = temp_CC + str(item)
            else:
                pass
        ccNum_data_list.append(temp_CC)

    titles = ['coords', 'dollars', 'CC_Num']
    data = [titles] + list(zip(coord_data_list, dollars_data_list, ccNum_data_list))

    for piece in data:
        line = '|'.join(str(x).ljust(10)for x in piece)
        full_data_list.append(line)

    return full_data_list

def isValidCC(passed_cc):
    """validates credit card number passed against regex listed
    arguments:
    passed_cc
    returns
    True or false depending on conditions met
    """
    ccRegex = re.compile(r'\b(4)(\d)(\d)(\s?)(\d)(\s?)(\d)(\d)(\s?)(\d)(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}(\s?)(\d){0,1}\b')
    ccTest = ccRegex.search(passed_cc)
    if ccTest is None:
        print("You did not enter a proper credit card. ")
        return False
    else:
        if passed_cc == ccTest.group():
            print("You entered a proper credit card. ")
            return True
        else:
            print("You did not enter a proper credit card. ")
            return False

def isValidCoord(passed_coord):
    """validates coordinates passed against regex listed
    arguments:
    passed_coord
    returns
    True or false depending on conditions met
    """
    coordRegex = re.compile(r'(-)?\b(\d?)(\d?)(\d?)\b(\.|,)\b(\d?)(\d?)(\d?)(\d?)(\d?)\b(, |; )(-)?\b(\d?)(\d?)(\d?)\b(\.|,)\b(\d?)(\d?)(\d?)(\d?)(\d?)\b')
    coordTest = coordRegex.search(passed_coord)
    if coordTest is None:
        print("You did not enter a proper coordinate. ")
        return False
    else:
        if passed_coord == coordTest.group():
            print("You entered a proper coord. ")
            return True
        else:
            print("You did not enter a proper coord. ")
            return False

def isValidDollar(passed_dollar):
    """validates dollar amount passed against regex listed
    arguments:
    passed_dollar
    returns
    True or false depending on conditions met
    """
    dollarRegex = re.compile(r'(\$ )(\d)(,|\.)(\d)(\d)(\d)')
    dollarTest = dollarRegex.search(passed_dollar)
    if dollarTest is None:
        print("You did not enter a proper dollar amount. ")
        return False
    else:
        if passed_dollar == dollarTest.group():
            print("You entered a proper dollar amount. ")
            return True
        else:
            print("You did not enter a proper dollar amount. ")
            return False