from application import db
from application.models import Base

class Response(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())




    responsename = db.Column(db.String(2000), nullable=False)
    text = db.Column(db.String(2000), nullable=False)


    article_id = db.Column(db.Integer, db.ForeignKey('article.id'),
                          nullable=False)

    def __init__(self, responsename, text):
        self.text = text
        self.responsename = responsename

