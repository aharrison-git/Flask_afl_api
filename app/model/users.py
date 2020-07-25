from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


    def __init__(self, username):
        self.username = username
        

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)
        #print(f"UsersModel: set_password:  password is: {password}, hash is: [{self.password}]")

    def check_password(self, password):
        #print(f"UsersModel:  check_password: password is: {password}, hash is: [{self.password}]")
        return check_password_hash(self.password, password)