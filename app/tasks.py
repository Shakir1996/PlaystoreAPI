from flask import Blueprint, jsonify
from app.models import App

scrape_playstore = Blueprint('scrape_playstore', __name__)


@scrape_playstore.route('/apps', methods=['GET'])
def get_apps():
    apps = App.query.all()
    app_list = []
    for app in apps:
        app_data = {
            'name': app.name,
            'category': app.category,
            'rating': app.rating,
            'reviews': app.reviews
        }
        app_list.append(app_data)
    return jsonify(app_list)
