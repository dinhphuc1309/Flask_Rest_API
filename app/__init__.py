from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # config database
    db.init_app(app)

    # config migrate
    migrate = Migrate(app, db)

    # config route
    from app.route.user_route import user_bp
    app.register_blueprint(user_bp)

    return app




