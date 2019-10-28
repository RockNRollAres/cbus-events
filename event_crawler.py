from selenium import webdriver
import time

# Initiate the web driver and destination webpage
exe_location = 'C:\\Python37\\WebDrivers\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=exe_location)

url = 'https://www.capa.com/events'
browser.get(url)
timeout = 5

# Navigate to the CAPA website and click "load more events" until none left.
while True:
    try:
        time.sleep(5)
        next_button = browser.find_element_by_id('loadMoreEvents')
        next_button.click()
        print("Loaded more events...")
    except:
        print('Maximum amount of events loaded.')
        break

# Save off the HTML after loading all events.
with open('capa.html', 'w') as f:
    page = browser.page_source
    f.write(page)
    print("HTML for page has been written to a file and saved.")

browser.close()

# capa_source = 'capa.html'
# capa_soup = BeautifulSoup(open(capa_source), 'html.parser')

## add in write to csv file
## maybe skip write to csv file, and go right to event create in gcal?

# os.unlink(capa_source)