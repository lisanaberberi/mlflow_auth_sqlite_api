from sqlite3 import Error
from db import create_connection

def select_all_users(cursor):
    """Query all rows in the users table."""
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        user_list = []
        for row in rows:
            user_list.append({
                "id": row[0],
                "username": row[1],
                "is_admin": row[3]
            })
        if not user_list:
            print("No records found in the 'users' table.")
        return user_list
    except Error as e:
        print(e)

def select_exp_permissions(cursor):
    """Query all rows in the experiment_permissions table."""
    try:
        cursor.execute("SELECT * FROM experiment_permissions")
        rows = cursor.fetchall()
        exp_permission_list = []
        for row in rows:
            exp_permission_list.append({
                "experiment_id": row[0],
                "user_id": row[1],
                "permission": row[2]
            })
        return exp_permission_list
    except Error as e:
        print(e)

def select_regModel_permissions(cursor):
    """Query all rows in the registered_model_permissions table."""
    try:
        cursor.execute("SELECT * FROM registered_model_permissions")
        rows = cursor.fetchall()
        regModel_permission_list = []
        for row in rows:
            regModel_permission_list.append({
                "model_name": row[0],
                "user_id": row[1],
                "permission": row[2]
            })
        return regModel_permission_list
    except Error as e:
        print(e)