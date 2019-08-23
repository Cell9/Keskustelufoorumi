from application import db
from application.models import Base
from flask_login import current_user

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)


    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    articles = db.relationship("Article", backref='account', lazy =True)
    groups = db.relationship("Groups", backref='groups', lazy =True)

    
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def find_linked_active_posts():
        stmt = text("SELECT Account.id, Article.postname FROM Account"
                    " JOIN Article ON Article.account_id = Account.id"
                    " GROUP BY Article.postname")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"":row[0], "postname":row[1]})

        return response
