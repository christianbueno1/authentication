import functools
#long lines can be broken over multiple lines using parenthesis
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#import models
from app.user_db_model import get_all_users, get_user, print_lst

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        print(f'post')
    # print(f"{get_db}")
    
    # try:
    #     conn = get_db()
    #     cur = conn.cursor()
    #     query = "select * from account"
    #     cur.execute(query)
    #     for row in cur:
    #         print(f"{row}")
    # except mariadb.Error as e:
    #     print(f"error database, auth.py: {e}")
    #     sys.exit(1)

    # user_lst = get_all_users()
    # print_lst(user_lst)
    user_foo = get_user(2)
    print(f"user_foo: {user_foo}")
        
    return 'register' 