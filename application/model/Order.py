from application.extensions import db


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('application_user_data.user_id'), nullable=False)
    user = db.relationship('ApplicationUser', backref='order')
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="Pending")  # Pending, Shipped, Delivered, Canceled
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    items = db.relationship('OrderItem', backref='order', lazy=True)

    def __init__(self, user_id, total_price, status="Pending"):
        self.user_id = user_id
        self.total_price = total_price
        self.status = status
        self.created_at = db.func.current_timestamp()
