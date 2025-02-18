from application.extensions import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)
    total_stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='products')

    def __init__(self, name, description, price, in_stock, total_stock, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock
        self.total_stock = total_stock
        self.image_url = image_url
        self.created_at = db.func.current_timestamp()
