import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time

def scrape_website(url):
    # Chrome driver auto install aur launch
#  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 driver = make_driver()
    # Website open karo
 try: 
       driver.get(url)
       print("Page Title and loading........", driver.title)
       html_content = driver.page_source
       human_pause(2, 5)
       return html_content
 except Exception as e:
       print("Error occurred:", e)
 finally:
       # Browser band karo
       driver.quit()
       

def human_pause(a=2, b=5):
    """Wait like a human (random between a and b seconds)."""
    t = random.uniform(a, b)
    print(f"[pause] waiting {t:.2f} seconds...")
    time.sleep(t)      




UA_POOL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
]

def make_driver():
    ua = random.choice(UA_POOL)   # pick a random UA
    print(f"[info] using UA: {ua}")

    opts = Options()
    opts.add_argument(f"--user-agent={ua}")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    return driver