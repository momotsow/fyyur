import os
SECRET_KEY = os.urandom(32)
# WTF_CSRF_ENABLED = False

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# postgres://{user}:{password}@{hostname}:{port}/{database-name}
# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/postgres'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True