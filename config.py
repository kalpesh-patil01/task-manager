import os
from dotenv import load_dotenv

# load the .env file 
load_dotenv()

class Config:
    # Flask app settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Kalpesh@1208'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:Kalpesh%40%231208@localhost:5432/task_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # debug setting
    DEBUG = True