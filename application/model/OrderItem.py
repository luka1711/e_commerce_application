from application.extensions import db


class OrderItem(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='order_items')
    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Column(db.Float, nullable=False)  # Store price at the time of purchase

    def __init__(self, order_id, product_id, quantity, price_at_purchase):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_at_purchase = price_at_purchase

