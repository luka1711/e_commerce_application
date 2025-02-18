from application.extensions import db, bcrypt


class ApplicationUser(db.Model):
    __tablename__ = 'application_user_data'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)  # Renamed to password_hash
    role = db.Column(db.String(10), default="customer")
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())  # Fix timestamp

    def __repr__(self):
        return f"<User {self.username}>"

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)  # Hash the password
        self.role = "customer"

    def set_password(self, password):
        """Hashes the password before storing it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)
