from bs4 import BeautifulSoup
import requests
import csv
import calendar_add

capa_source = requests.get('https://www.capa.com/events').text

capa_soup = BeautifulSoup(capa_source, 'lxml')
events = capa_soup.find_all('div', class_='info clearfix')

output_file = open('events.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['Date', 'Title', 'Location'])

for event in events:
	title = event.h3.text
	date = event.find('div', class_='date').text
	location = event.find('span', class_='venue-title').a.text
	output_writer.writerow([date.strip(), title.strip(), location.strip()])

# TO DO: Pull event list from 'https://promowestlive.com/columbus'

output_file.close()