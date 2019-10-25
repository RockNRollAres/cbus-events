from bs4 import BeautifulSoup
import requests
import csv
import os

from selenium import webdriver
import time

# Initiate the web driver and destination webpage
##### exe_location = 'REPLACE WITH LOCAL PATH FOR chromedriver.exe'
browser = webdriver.Chrome(executable_path=exe_location)

url = 'https://www.capa.com/events'
browser.get(url)
timeout = 5

# Navigate to the CAPA website and click "load more events" until all are there.
while True:
	try:
		time.sleep(5)
		next_button = browser.find_element_by_id('loadMoreEvents')
		next_button.click()
		print('Loaded more events...')
	except:
		print('Maxiumum amount of events loaded.')
		break

# Save off the HTML after loading all events.
with open('capa.html', 'w') as f:
	page = browser.page_source
	f.write(page)
	print('HTML for page has been written to file and saved.')


capa_source = 'capa.html'
capa_soup = BeautifulSoup(open(capa_source), 'html.parser')

events = capa_soup.find_all('div', class_='info clearfix')

output_file = open('events.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['Date', 'Title', 'Location'])

for event in events:
	title = event.h3.text
	date = event.find('div', class_='date').text
	location = event.find('span', class_='venue-title').a.text
	output_writer.writerow([date.strip(), title.strip(), location.strip()])

output_file.close()

os.unlink(capa_source)
