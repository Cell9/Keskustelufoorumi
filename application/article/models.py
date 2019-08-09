from application import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    name = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(144), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.active = False
        self.email = email
