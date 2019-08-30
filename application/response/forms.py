from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, BooleanField,  TextAreaField, validators

class ResponseForm(FlaskForm):
    responsename = StringField("Title:", [validators.DataRequired()])
    text = TextAreaField('Text:', [validators.DataRequired()] , render_kw={"rows": 14, "cols": 60}) 
 
    class Meta:
        csrf = False
