from sqlite3 import Error
from fastapi import FastAPI
from db import create_connection
from users import select_all_users, select_regModel_permissions, select_exp_permissions
import uvicorn

from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/users/")
def get_all_users():
    try:
        conn, cursor = create_connection("/basic_auth.db")
        user_list = select_all_users(cursor)
        cursor.close()
        conn.close()
        print(user_list)
        return {"users": user_list}
    except Exception as e:
        return {"error": str(e)}

# Define a new endpoint for permissions
@app.get("/experiment-permissions/")
def get_exp_permissions():
    try:
        conn, cursor = create_connection("/basic_auth.db")
        permission_list = select_exp_permissions(cursor)
        cursor.close()
        print(permission_list)
        conn.close()
        print(permission_list)
        return {"permissions": permission_list}
    except Exception as e:
        return {"error": str(e)}

@app.get("/registered-models-permissions/")
def get_regModel_permissions():
    try:
        conn, cursor = create_connection("/basic_auth.db")
        permission_list = select_regModel_permissions(cursor)
        cursor.close()
        conn.close()
        print(permission_list)
        return {"permissions": permission_list}
    except Exception as e:
        return {"error": str(e)}

def main():
    try:
        print("2. Query all users")
        get_all_users()
        get_exp_permissions()
        get_regModel_permissions()

    except Error as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
