from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, models, login_required
from application.groups.models import Groups
from application.groups.forms import GroupsForm

@app.route("/groups/", methods=["GET"])
@login_required()
def groups_list():
    return render_template("groups/list.html", groups = Groups.query.all())

@app.route("/groups/new/")
@login_required()
def groups_form():
    return render_template("groups/new.html", form = GroupsForm())


@app.route("/groups/<groups_id>/", methods=["POST"])
@login_required(role="ANY" or "ADMIN")
def groups_join(groups_id):

        t = Groups.query.get(groups_id)
        t.account_id = current_user.id
        
        
        db.session().add(t)
        db.session().commit()
        

        return redirect(url_for("index"))

@app.route("/groups/", methods=["POST"])
@login_required(role="ANY" or "ADMIN")
def groups_create():
    form = GroupsForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)    
    members = current_user.id
    t = Groups(form.name.data, form.desc.data, members)
    t.account_id = current_user.id
 
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("index"))
