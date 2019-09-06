from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, validators
from wtforms.widgets import TextArea

class ResponseForm(FlaskForm):
    text = TextAreaField('Text:', [validators.Length(min=2, max = 2000)], render_kw={"rows": 14, "cols": 60}, widget=TextArea()) 
 
    class Meta:
        csrf = False
