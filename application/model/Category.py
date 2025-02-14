from application.db import db


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, category_name, category_id):
        self.category_name = category_name
        self.category_id = category_id
        self.created_at = db.func.current_timestamp()
