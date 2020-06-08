from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = self.set_password(password)


    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)