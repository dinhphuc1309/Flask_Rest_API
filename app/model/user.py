from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, name='user_name')
    email = db.Column(db.String(120), unique=True, nullable=False)
