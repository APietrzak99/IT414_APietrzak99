from selenium import webdriver
import os
import shutil

my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/index.php")

#this will test that the first name, last name, and phone number inputs will throw an error when required fields are left blank

my_browser.save_screenshot("images/blank_test.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

block_alert = my_browser.switch_to.alert
block_text = block_alert.text
block_alert.accept()

#this will test that the first name, last name, and phone number inputs will throw an error when not enough characters are entered

f_name_field = my_browser.find_element_by_id("firstName")
f_name_field.send_keys("an")

l_name_field = my_browser.find_element_by_id("lastName")
l_name_field.send_keys("a")

phone_field = my_browser.find_element_by_id("phoneNumber")
phone_field.send_keys("586246229")

my_browser.save_screenshot("images/short_input_test.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

error_alert = my_browser.switch_to.alert
error_alert.accept()

#this will test that the first name, last name, and phone number inputs will throw an error when too many characters are entered

f_name_field.clear()
f_name_field.send_keys("anthonypietrzak")

l_name_field.clear()
l_name_field.send_keys("marcusdavidwallace")

phone_field.clear()
phone_field.send_keys("586243546348744")

my_browser.save_screenshot("images/long_input_test.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

error_alert = my_browser.switch_to.alert
error_alert.accept()

#this will test the phone number input being valid at 10 characters, but will also test the email field format being invalid
#the first and last name fields should be at a valid length

f_name_field.clear()
f_name_field.send_keys("anthony")

l_name_field.clear()
l_name_field.send_keys("pietrzak")

email_field = my_browser.find_element_by_id("emailAddress")
email_field.send_keys("anthonypietrzak")

phone_field.clear()
phone_field.send_keys("5862789608")

my_browser.save_screenshot("images/phone_and_email_input_test.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

error_alert = my_browser.switch_to.alert
error_alert.accept()

#this will test the phone number input being valid at 12 characters, but will also test the email field format being invalid
#the first and last name fields should be valid

phone_field.clear()
phone_field.send_keys("586-278-9608")

my_browser.save_screenshot("images/phone_and_email_input_test2.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

error_alert = my_browser.switch_to.alert
error_alert.accept()

#this will test all inputs being valid, most specifically, will test the email field format to be valid, as the rest of the fields are already valid

email_field.clear()
email_field.send_keys("apietrza@walshcollege.edu")

my_browser.save_screenshot("images/valid_test.png")
submit_button = my_browser.find_element_by_id("my_submit")
submit_button.click()

my_work_dir = os.getcwd()

button_text = my_browser.find_element_by_link_text("Go Back")

if button_text:
    my_return = os.walk(os.path.join(my_work_dir,"images"))
    for item in my_return:
        for filename in item[2]:
            if filename == "valid_test.png":
                temp_filename = "passed_" + filename
                shutil.move(os.path.join(item[0], filename), os.path.join(item[0], temp_filename))


