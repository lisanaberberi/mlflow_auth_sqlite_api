from sqlite3 import connect, Error

def create_connection(db_file):
    """Create a database connection and cursor to the SQLite database."""
    conn, cursor = None, None
    try:
        conn = connect(db_file)
        cursor = conn.cursor()
        print("connection success")
    except Error as e:
        print(e)
    return conn, cursor
