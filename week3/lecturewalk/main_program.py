import os 
import shutil

# for folderName, subFolders, filenames in os.walk('C:\\file_explore'):
#     print("The current folder is " + folderName)

my_return = os.walk('C:\\file_explore')

for item in my_return:
    for filename in item[2]:
        temp_filename = "orig_" + filename
        shutil.move(os.path.join(item[0], filename), os.path.join(item[0], temp_filename))

