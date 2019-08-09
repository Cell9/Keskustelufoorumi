from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.article.models import Article
from application.article.forms import UserForm

@app.route("/article/", methods=["GET"])
def article_index():
    return render_template("article/list.html", article = Article.query.all())

@app.route("/article/new/")
def article_form():
    return render_template("article/new.html", form = UserForm())


@app.route("/article/<article_id>/", methods=["POST"])
@login_required
def article_active(article_id):

    t = Article.query.get(article_id)
    if t.active == False:
        t.active = True
    else:
        t.active = False


    db.session().commit()
  
    return redirect(url_for("article_index"))

@app.route("/article/", methods=["POST"])
@login_required
def article_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("article/new.html", form = form)    
    
    t = Article(form.name.data,form.email.data)
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("article_index"))
