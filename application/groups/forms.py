from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, TextAreaField, validators

class GroupsForm(FlaskForm):
    name = StringField("Group name:", [validators.DataRequired()])
    desc = TextAreaField('Description:', [validators.DataRequired()] , render_kw={"rows": 15, "cols": 40}) 
 
    class Meta:
        csrf = False
