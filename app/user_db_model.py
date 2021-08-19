# import mariadb
# from flask import current_app, g
from .user_model import User
# from .db_model import get_db, mariadb, get_db1
from .db_model import mariadb, get_db1
# from app.user_model import User
import sys

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

#cur.fetchmany() #default 1 row
#cur.fetchmany(5)

#crud: create, retrieve, update, delete

#from list of tuples, fetchall
#to list of User class
def to_user_lst(list_):
    user_lst = []
    for tuple_ in list_:
        user_obj = tpl_to_user_obj(tuple_)
        user_lst.append(user_obj)
    return user_lst

#print all user
#from list of user class
def print_user_lst(user_lst):
    for user_obj in user_lst:
        print(f"{user_obj}")
        print()

def tpl_to_user_obj(user_tpl):

    # user_dict = dict(
    #     id = tuple_[0],
    #     username = tuple_[1],
    #     email = tuple_[2],
    #     password = tuple_[3],
    #     fname = tuple_[4],
    #     lname = tuple_[5],
    #     dob = tuple_[6]
    # )
    # user_obj = User(**user_dict)

    user_obj = User(
        id=user_tpl[0], 
        username=user_tpl[1],
        email=user_tpl[2],
        password=user_tpl[3],
        fname=user_tpl[4],
        lname=user_tpl[5],
        dob=user_tpl[6]
    )
    return user_obj

#retrieve
#return a list of user class
#if doesn't find any return None
def get_all_users():
    try:
        conn = get_db1()
        #use connection
        cur = conn.cursor()
        query = "select * from account"
        cur.execute(query)
        fetchall_lst = cur.fetchall()
    except mariadb.Error as e:
        print(f"get_all_users method: {e}")
        #sys.exit(0) #ok
        # database issues, I use exit code 1
        sys.exit(1)
    finally:
        #close connection
        cur.close()
        conn.close()
        
        if not fetchall_lst:
            return None
        user_lst = to_user_lst(fetchall_lst) 
    return user_lst

#retrieve
#Return a User object, if doens't find one return None
#when resulset is empty fetchone() return None
def get_user(id):
    try:
        conn = get_db1()
        # use connection
        cur = conn.cursor()
        query = "select * from account where id=?"
        # #id as tuple
        cur.execute(query, (id,))
        #return a tuple
        user_tpl = cur.fetchone()
        
    except mariadb.Error as e:
        print(f"Error connecting to mariadb platform: {e}")
        sys.exit(1)
    finally:
        #close connection
        cur.close()
        conn.close()

    if not user_tpl:
        return None
    user_obj = tpl_to_user_obj(user_tpl)
    return user_obj

#create
# arguments required:username, email, password
# def insert_user(cur, user_obj):
def insert_user(user_obj):
    try:
        #use connection
        conn = get_db1()
        cur = conn.cursor()

        #spanning string over multiple lines
        #triple quotes
        #ignore end of lines with \
        query = """\
            insert into account \
            (username, email, password, fname, lname, dob) \
            values \
            (?,?,?,?,?,?)"""
        # query = "insert into account (username, email, password, fname, lname, dob) values (?,?,?,?,?,?)"
        cur.execute(query, (user_obj.username, user_obj.email, user_obj.password, user_obj.fname, user_obj.lname, user_obj.dob))
        conn.commit()    
    except mariadb.Error as e:
        print(f"Error connecting to mariadb platform: {e}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

# def insert_user2(user_obj):
#     try:
#         conn = get_db1()
#         cur = conn.cursor()
#         query = "insert into account (username, email, password, fname, lname, dob) values (?,?,?,?,?,?)"
#         cur.execute(query, (user_obj.username, user_obj.email, user_obj.password, user_obj.fname, user_obj.lname, user_obj.dob))
#         conn.commit()
#     except mariadb.Error as e:
#         print(f"Error connecting to mariadb platform: {e}")
#         sys.exit(1)
#     finally:
#         cur.close()
#         conn.close()

#update
def update_user(id, new_fname, new_lname, new_dob):
    try:
        conn = get_db1()
        cur = conn.cursor()
        query = "update account set fname=?, lname=?, dob=? where id=?"
        cur.execute(query, (new_fname, new_lname, new_dob, id))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error connecting to mariadb platform: {e}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

#change username or create username
#verify availability of username
#if there is no username return None
def get_by_username(username):
    try:
        conn = get_db1()
        cur = conn.cursor()
        query = "select * from account where username=?"
        cur.execute(query, (username,))
        user_tpl = cur.fetchone()
        
    except mariadb.Error as e:
        print(f"Error connecting to mariadb platform: {e}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

    if not user_tpl:
        return None
    user_obj = tpl_to_user_obj(user_tpl)
    return user_obj

# try:
#     conn = get_db1()
#     cur = conn.cursor()
# except mariadb.Error as e:
#     print(f"Error connecting to mariadb platform: {e}")
#     sys.exit(1)
# finally:
#     cur.close()
#     conn.close()

def get_by_email(email):
    try:
        conn = get_db1()
        cur = conn.cursor()
        query = "select * from account where email=?"
        cur.execute(query, (email,))
        user_tpl = cur.fetchone()
    except mariadb.Error as e:
        print(f"Error connecting to mariadb platform: {e}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

    if not user_tpl:
        return None
    user_obj = tpl_to_user_obj(user_tpl)
    return user_obj

