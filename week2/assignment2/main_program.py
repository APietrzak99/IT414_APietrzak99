from functions.filesystem_functions import drawmenu
from functions.filesystem_functions import copyFolder

program_running = True

while program_running:

    drawmenu()

    my_option = input("What is your selection? ")

    if my_option.lower() == "c":
        copyFolder()
    else:
        print("You did not type a valid response. ")

    done_running = input("Would you like to do something else? (Y/N) ")

    if done_running.lower() == "n":
        program_running = False