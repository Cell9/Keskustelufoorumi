from flask import render_template
from application import app
from application.auth.models import User
from application.article.models import Article

@app.route('/')
def index():
    return render_template("index.html", active_posts=User.find_active_posts())
