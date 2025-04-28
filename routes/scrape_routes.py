# routes/scrape_routes.py

from flask import Blueprint, request, jsonify
from controllers.scrape_controller import get_scraped_data

scrape_routes = Blueprint('scrape_routes', __name__)

@scrape_routes.route('/scrape', methods=['GET'])
def scrape():
    query = request.args.get('query')
    data, status = get_scraped_data(query)
    return jsonify(data), status
