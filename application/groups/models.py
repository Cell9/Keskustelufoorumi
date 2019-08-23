from application import db
from application.models import Base

class Groups(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
	
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


    def __init__(self, name, desc, members):
        self.name = name
        self.desc = desc
        self.members = desc
