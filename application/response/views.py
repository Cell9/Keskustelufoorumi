from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required, login_manager
from application.article.models import Article
from application.response.models import Response
from application.response.forms import ResponseForm



@app.route("/response/<article_id>/new", methods=["GET","POST"])
@login_required(role="ANY" or "ADMIN")
def response_create(article_id):
    if request.method == "GET":
        return render_template("/response/new.html", form=ResponseForm(), article_id=article_id)

    
    form = ResponseForm(request.form)
    if not form.validate():
        return render_template("/response/new.html",form = form, article_id=article_id)    

    
    t = Response(form.text.data)
    t.article_id = article_id
    t.account_id = current_user.id

    
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("article_view", article_id=article_id))


