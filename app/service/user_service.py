from app.model.user import User
from app import db

def get_all_users():
    users = User.query.all()
    return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return {'id': user.id, 'username': user.username, 'email': user.email}
    else:
        return None

def create_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return {'id': new_user.id, 'username': new_user.username, 'email': new_user.email}
