from functions.regex_functions import findAllData
import pyperclip

data_string = str(pyperclip.paste())

my_data = findAllData(data_string)

for line in my_data:
    print(line + "\n")

output_string = ""

for line in my_data:
    output_string = output_string + line + "\n"

pyperclip.copy(output_string)