# from app.db_model import get_db
from datetime import datetime,date
import bcrypt
import functools
#long lines can be broken over multiple lines using parenthesis
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#import models
# from app.user_db_model import get_all_users, get_user, insert_user, print_user_lst, User, get_db, insert_user2
from app.user_db_model import get_all_users, get_user, insert_user, print_user_lst, User, update_user

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
    # print_user_lst(user_lst)

    # user_foo = get_user(2)
    # print(f"user_foo: {user_foo}")

    # conn = get_db()
    # cur = conn.cursor()

    #encode the string as binary
    # my_pass = b'12345'
    # my_pass = '!@#'.encode('utf-8')
    # password = request.form.get("password").encode("utf-8")
    # my_pass_hash = bcrypt.hashpw(my_pass, bcrypt.gensalt())

    # dob = datetime(1985,1,16)
    # dob = date.today()
    # dob = date(1985,2,28)
    # user_obj3 = User(0, 'chris', 'chris@ibm.ec', my_pass_hash, 'Christian', 'Bueno', dob)
    # user_obj3 = User()
    # user_obj3.username = 'ruth'
    # user_obj3.email = 'ruth@ibm.ec'
    # user_obj3.password = my_pass_hash
    # user_obj3.fname = 'Ruth'
    # user_obj3.lname = 'Ronaldo'
    # user_obj3.dob = dob
    # print(f"user_obj3: {user_obj3}")
    # insert_user(cur, user_obj3)
    
    # insert_user(user_obj3)
    # print(f"user inserted")
    update_user(13, 'Chris2', 'Bueno', date(1985,1,16))
    print(f"user updated")
        
    return 'register' 