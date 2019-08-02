from application import app, db
from flask import redirect, render_template, request, url_for
from application.kayttaja.tiedot import Kayttaja

@app.route("/kayttaja/", methods=["GET"])
def kayttaja_index():
    return render_template("kayttaja/list.html", kayttaja = Kayttaja.query.all())

@app.route("/kayttaja/new/")
def kayttaja_form():
    return render_template("kayttaja/new.html")

@app.route("/kayttaja/<kayttaja_id>/", methods=["POST"])
def kayttaja_delete(kayttaja_id):

    t = Kayttaja.query.get(kayttaja_id)
	
    db.session().delete(t)    
    db.session().commit()
  
    return redirect(url_for("kayttaja_index"))

@app.route("/kayttaja/", methods=["POST"])
def kayttaja_create():
    t = Kayttaja(request.form.get("name"))
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("kayttaja_index"))
