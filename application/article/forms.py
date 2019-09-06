from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, BooleanField,  TextAreaField, validators

class ArticleForm(FlaskForm):
    postname = StringField("Article name:", [validators.Length(min=2, max = 80)])
    active = BooleanField("Inactive:")
    text = TextAreaField('Text:', [validators.Length(min=2, max = 2000)], render_kw={"rows": 15, "cols": 70}) 
 
    class Meta:
        csrf = False
