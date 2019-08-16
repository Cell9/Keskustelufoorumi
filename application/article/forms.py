from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, BooleanField,  TextAreaField, validators

class ArticleForm(FlaskForm):
    postname = StringField("Article name:", [validators.DataRequired()])
    active = BooleanField("Active")
    text = TextAreaField('Text', [validators.DataRequired()] , render_kw={"rows": 70, "cols": 15}) 
 
    class Meta:
        csrf = False
