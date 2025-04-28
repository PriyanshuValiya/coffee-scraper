# controllers/scrape_controller.py

from utils.scraper import scrape_google_maps

def get_scraped_data(query):
    if not query:
        return {"error": "Query parameter is missing."}, 400
    
    data = scrape_google_maps(query)
    return data, 200
