from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.article.models import Article
from application.article.forms import ArticleForm

@app.route("/article/", methods=["GET"])
def article_index():
    return render_template("article/list.html", article = Article.query.all())

@app.route("/article/new/")
def article_form():
    return render_template("article/new.html", form = ArticleForm())


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
    form = ArticleForm(request.form)

    if not form.validate():
        return render_template("article/new.html", form = form)    
    
    t = Article(form.postname.data, form.active.data, form.text.data)
    t.account_id = current_user.id
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("article_index"))
