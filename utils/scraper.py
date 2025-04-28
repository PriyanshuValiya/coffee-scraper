# utils/scraper.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.browser import create_browser

def scrape_google_maps(query):
    driver = create_browser()

    try:
        url = f"https://www.google.com/maps/search/{query}"
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hfpxzc')))

        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)

        businesses = driver.find_elements(By.CLASS_NAME, 'hfpxzc')

        results = []
        for biz in businesses:
            try:
                name = biz.find_element(By.CLASS_NAME, 'fontHeadlineSmall').text
            except:
                name = None
            try:
                address = biz.find_element(By.CLASS_NAME, 'UsdlK').text
            except:
                address = None
            try:
                phone = biz.find_elements(By.CLASS_NAME, 'UsdlK')[1].text
            except:
                phone = None

            results.append({
                'name': name,
                'address': address,
                'phone': phone,
                'email': None
            })

        return results

    finally:
        driver.quit()
