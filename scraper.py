# import selenium.webdriver as webdriver
# from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome driver auto install aur launch
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Website open karo
driver.get("https://www.google.com")

print("Page Title:", driver.title)

# Browser band karo
driver.quit()
