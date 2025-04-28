# app.py

from flask import Flask
from routes.scrape_routes import scrape_routes

app = Flask(__name__)

# Register the routes
app.register_blueprint(scrape_routes)

if __name__ == '__main__':
    app.run(debug=True)
