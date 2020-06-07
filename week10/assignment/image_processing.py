from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
import requests
from bs4 import BeautifulSoup
import os
from os.path import basename
import shutil
from functions.image_function import image_logo_draw
import zipfile

#remove all files in images directory
shutil.rmtree("images/")
os.makedirs("images/")

#enter website with images we need
site = 'https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week10/WI20-Assignment/employees/index.php'

#pull site data
response = requests.get(site)

#find all images with an html parser
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
employee_tags = soup.find_all("h5")

employee_info = []

#grab urls of images for downloading later
urls = [img['src'] for img in img_tags]

for item in employee_tags:
    employee_info.append(item.get_text())

#alphabetize list so correct labels go to correct images
employee_info = sorted(employee_info)

#this will format the urls so that it will use the correct url when attempting to download the images from the website
for url in urls:
    with open("images/" + url[4:], 'wb') as img:
        url = '{}{}'.format(site[:-9], url)
        response = requests.get(url)
        img.write(response.content)

#locate file name with logo in it so that we can determine which img is the logo img
logoimstr = []

keyword = 'logo'
for fname in os.listdir('images/'):
    if keyword in fname:
        logoimstr.append(fname)

#variable to setup looping through employee_info list 
employee_num=0

#loop through all files in images, and then pass the variables to image_logo_draw for image manipulation
for path,name,filenames in os.walk('images/'):
    for fname in filenames:
        if keyword not in fname:
            if not os.path.isdir("images/output_images"):
                os.makedirs("images/output_images")
                image_logo_draw(logoimstr[0],fname,employee_info[employee_num])
                employee_num += 1
            else:
                image_logo_draw(logoimstr[0],fname,employee_info[employee_num])
                employee_num +=1

#create zip file and write output_images folder to the archive
employeeZip = zipfile.ZipFile('images/employee_images.zip', "w")

for root, dirs, files in os.walk('images/output_images'):
  for filename in files:
    employeeZip.write(os.path.join(root, filename))