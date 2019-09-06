from application import db
from application.auth.models import User

from sqlalchemy import event

@event.listens_for(User.__table__, "after_create")
def insert_initial_values(*args, **kwargs):
    db.session.add(User("Admin", "admin", "admin@gmail.com", "admin"))

    db.session.commit()
