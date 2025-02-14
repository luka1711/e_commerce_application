from application.db import db


class User(db.Model):
    __tablename__ = 'application_user_data'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), default="customer")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.role = "customer"
        self.created_at = db.func.current_timestamp()