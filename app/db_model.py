import mariadb
from flask import current_app, g
from .user_model import User
# from app.user_model import User
# import click
# from flask.cli import with_appcontext

import sys


def get_db():
    if 'db' not in g:
        
        #create a dictionary
        # d = {'a': 'one', 'b': 'two'}
        database_credentials = dict(
            user=current_app.config['DATABASE_USER'],
            host=current_app.config['DATABASE_HOST'],
            port=current_app.config['DATABASE_PORT'],
            password=current_app.config['DATABASE_PASSWORD'],
            db=current_app.config['DATABASE_DB']
        )
        #unpack values from dictionary with **database_credentials
        g.db = mariadb.connect(**database_credentials)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)