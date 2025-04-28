# utils/browser.py

from selenium import webdriver

def create_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')    # Headless mode (no browser UI)
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    return driver
