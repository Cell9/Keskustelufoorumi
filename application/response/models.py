from application import db
from application.models import Base
from application.article.models import Article
from sqlalchemy.sql import text

class Response(Base):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())



    text = db.Column(db.String(2000), nullable=False)

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, text):
        self.text = text
        


    @staticmethod
    def get_comments_in_article(article_id):
          statement = text("SELECT Account.id, Account.username, Response.id, Response.text, Response.date_created FROM Response"
                      " LEFT JOIN Article ON Article.id = Response.article_id"
                      " LEFT JOIN Account ON Account.id = Response.account_id"
                      " WHERE Article.id = :article_id"
                      " ORDER BY  Response.date_created ASC").params(article_id=article_id)
          res = db.engine.execute(statement)

          response = []
          for row in res:
             response.append([row[0], row[1], row[2], row[3], row[4]]);

          return response
