import os
from dotenv import load_dotenv

load_dotenv()

SCRAPINGBEE_API_KEY = os.getenv("SCRAPINGBEE_API_KEY")
BASE_URL = "https://app.scrapingbee.com/api/v1/"
