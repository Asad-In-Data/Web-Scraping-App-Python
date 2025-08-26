import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

def scrape_website(url):
    # Chrome driver auto install aur launch
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Website open karo
 try: 
       driver.get(url)
       print("Page Title and loading........", driver.title)
       html_content = driver.page_source
       time.sleep(20)
       
       return html_content
 except Exception as e:
       print("Error occurred:", e)
 finally:
       # Browser band karo
       driver.quit()
       
