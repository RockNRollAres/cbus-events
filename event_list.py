from bs4 import BeautifulSoup
import requests
import csv

capa_source = requests.get('https://www.capa.com/events').text

capa_soup = BeautifulSoup(capa_source, 'lxml')
events = capa_soup.find_all('div', class_='info clearfix')

output_file = open('events.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['Date', 'Title', 'Location'])

for event in events:
	# check = input("\nNext?   ")
	# if check != 'n':
	title = event.h3.text
	date = event.find('div', class_='date').text
	location = event.find('span', class_='venue-title').a.text
	# print(f"Date: {date.strip()}")
	# print(f"Event: {title.strip()}")
	# print(f"Location: {location.strip()}\n")
	output_writer.writerow([date.strip(), title.strip(), location.strip()])
	# else:
	# 	break

output_file.close()