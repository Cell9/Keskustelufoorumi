from application import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    postname = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.String(2000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, postname, active, text):
        self.postname = postname
        self.active = True
        self.text = text
