from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

env_file = os.getenv('FLASK_ENV', 'development') + '.env'
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), env_file))
print(os.path.dirname(__file__))

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '3306')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'site_db')

encoded_password = quote_plus(DATABASE_PASSWORD)

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DATABASE_USER')}:{quote_plus(os.getenv('DATABASE_PASSWORD'))}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"