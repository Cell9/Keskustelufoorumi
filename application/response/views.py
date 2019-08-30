from flask import redirect, render_template, request, url_for
from flask_login import  current_user

from application import app, db, login_required
from application.response.models import Response
from application.response.forms import ResponseForm


@app.route("/response/new/")
def response_form():
    return render_template("/response/new.html", form = ResponseForm())


@app.route("/response/", methods=["GET","POST"])
@login_required(role="ANY" or "ADMIN")
def response_create():
    
    form = ResponseForm(request.form)

    if not form.validate():
        return render_template("/response/new.html",form = form)    
    
    t = Response(form.responsename.data, form.text.data)

    t.article_id = Article.query.get()
    
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("article_index"))


