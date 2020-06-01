from functions.functions import *
import json
import psutil

with open("text_files/script_config.json", "rb") as config:
    reading = config.read()
    data = json.loads(reading)

values_list = []

for item in data:
    for key, value in item.items():
        values_list.append(value)

disk_usage(values_list[6],values_list[7],values_list[8],values_list[9])
ram_usage(values_list[6],values_list[7],values_list[8],values_list[9])
cpu_usage(values_list[6],values_list[7],values_list[8],values_list[9])
network_packets(values_list[6],values_list[7],values_list[8],values_list[9])