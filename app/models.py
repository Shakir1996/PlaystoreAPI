from app import db


class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<App {self.name}>"
