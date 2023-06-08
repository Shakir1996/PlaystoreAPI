from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playstore.db'
db: SQLAlchemy = SQLAlchemy(app)


class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255))
    developer = db.Column(db.String(255))
    category = db.Column(db.String(255))

    def __repr__(self):
        return f'<App {self.package_name}>'


@app.route('/')
def index():
    # Retrieve data from the database
    apps = App.query.all()
    return {'apps': [app.package_name for app in apps]}


if __name__ == '__main__':
    app.run(debug=True)
