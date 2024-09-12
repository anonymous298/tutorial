# config.py

import os

# Configuration for MySQL database
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://<root>:<ACCER1990@>@localhost/<Practice>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress warnings
