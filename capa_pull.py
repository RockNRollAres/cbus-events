# Load all events on the CAPA page and save off the html

from selenium import webdriver
import time

## Navigate to the CAPA website and click the "load more" button
####### Add chromedriver.exe to laptop path and replace in below exe_location ######
# exe_location = '../chromedriver.exe'
browser = webdriver.Chrome(executable_path=exe_location)

url = 'https://www.capa.com/events'
browser.get(url)
timeout = 5

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
