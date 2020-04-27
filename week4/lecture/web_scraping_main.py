import requests
from bs4 import BeautifulSoup

# my_url = input("Please enter a URL: ")
# request = requests.get(my_url)

# if request.status_code == 200:
#     weather_data = open("downloads/weather_data.html", "wb")
#     for data_chunk in request.iter_content(100000):
#         weather_data.write(data_chunk)

my_weather_page = open("downloads/weather_data.html")

weather_soup = BeautifulSoup(my_weather_page, "lxml")

my_days = weather_soup.findAll("span", {"class": ["day-detail", "clearfix"]})

my_temps = weather_soup.findAll("td", {"class": ["temp"]})

my_title = weather_soup.find("h1")

print(my_title.getText())

# counter = 0

# while counter < len(my_days):
#     print(my_days[counter].getText())
#     hi_lo_temp = my_temps[counter].findAll("span")
#     hi_temp_unicode = hi_lo_temp[0].getText()
#     hi_temp = ""
#     for char in hi_temp_unicode:
#         if char.isdigit():
#             hi_temp = hi_temp + char
#     print(hi_temp)
#     lo_temp_unicode = hi_lo_temp[2].getText()
#     lo_temp = ""
#     for char in lo_temp_unicode:
#         if char.isdigit():
#             lo_temp = lo_temp + char
#     print(lo_temp)
#     print(my_temps[counter].get("title"))
#     counter += 1