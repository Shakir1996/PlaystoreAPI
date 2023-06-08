from flask import jsonify
from app.models import App
from app.routes import bp
from sqlalchemy import or_


@bp.route('/')
def home():
    apps = App.query.filter(or_(App.app.X2L60.like("%com"%".games%"),
                                )).all()
    app_names = [app.title for app in apps]  # Extract the names of the apps

    return jsonify({'apps': app_names})
