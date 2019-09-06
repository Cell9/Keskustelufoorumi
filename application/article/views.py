from flask import redirect, render_template, request, url_for
from flask_login import  current_user

from application import app, db, login_required
from application.article.models import Article
from application.response.models import Response
from application.article.forms import ArticleForm

@app.route("/article/", methods=["GET"])
def article_index():
    return render_template("article/list.html", article = Article.query.all())

@app.route("/article/<article_id>", methods=["GET"])
@login_required(role="ANY" or "ADMIN")
def article_view(article_id):

    responseData = Response.get_comments_in_article(article_id)
    
    return render_template("article/post.html", article = Article.query.get(article_id), article_id = article_id, responseData=responseData)



@app.route("/article/<article_id>/", methods=["POST"])
@login_required(role="ADMIN")
def article_active(article_id):

    t = Article.query.get(article_id)
    if t.active == False:
        t.active = True
    else:
        t.active = False


    db.session().commit()
  
    return redirect(url_for("article_index"))

@app.route("/article/new", methods=["GET", "POST"])
@login_required(role="ANY" or "ADMIN")
def article_create():
    
    if request.method == "GET":
        return render_template("article/new.html", form=ArticleForm())

    form = ArticleForm(request.form)
    if not form.validate():
        return render_template("article/new.html", form = form)    
    
    t = Article(form.postname.data, form.active.data, form.text.data)
    t.account_id = current_user.id
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("article_index"))

@app.route("/article/<article_id>/delete/", methods=["GET"])
@login_required(role="ADMIN")
def article_delete(article_id):

    responseData = Response.get_comments_in_article(article_id)
    for row in responseData:
      Res = Response.query.get(row[2])
      db.session().delete(Res)
    
    t = Article.query.get(article_id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("article_index"))
