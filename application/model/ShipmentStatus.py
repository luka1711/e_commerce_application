from application.extensions import db


class ShipmentStatus(db.Model):
    __tablename__ = 'shipment_status'

    status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, status_name, status_id):
        self.status_name = status_name
        self.status_id = status_id