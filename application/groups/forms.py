from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, TextAreaField, validators

class GroupsForm(FlaskForm):
    name = StringField("Group name:", [validators.Length(min=2, max=50)])
    desc = TextAreaField('Description:', [validators.Length(min=2, max=1000)] , render_kw={"rows": 15, "cols": 80}) 
 
    class Meta:
        csrf = False
