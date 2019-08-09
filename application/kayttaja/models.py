from application import db

class Kayttaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    name = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.active = False
