from application.db import db


class Shipping(db.Model):
    __tablename__ = 'shipping'
    shipment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    order = db.relationship('Order', backref='Shipping')
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('shipment_status.id'), nullable=False)
    status = db.relationship('ShipmentStatus', backref='Shipping')
    shipped_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, shipment_id, order_id, address, city, state, country, postal_code, shipped_at, status_id, status):
        self.shipment_id = shipment_id
        self.order_id = order_id
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.shipped_at = shipped_at

