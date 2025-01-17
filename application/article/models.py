from application import db
from application.models import Base


class Article(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    postname = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.String(2000), nullable=False)

    responses = db.relationship("Response", backref='article', lazy =True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, postname, active, text):
        self.postname = postname
        self.active = True
        self.text = text

