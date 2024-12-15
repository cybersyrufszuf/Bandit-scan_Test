import sqlite3
from hashlib import sha256

def connect_to_database(db_name):
    """
    Connect to the SQLite database securely.
    """
    try:
        conn = sqlite3.connect(db_name)
        print("Database connection established.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table(conn):
    """
    Create a secure user table if it doesn't already exist.
    """
    try:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                )
                """
            )
            print("Table 'users' created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_user(conn, username, password):
    """
    Insert a new user into the database securely.
    """
    try:
        # Hash the password before storing it
        password_hash = sha256(password.encode()).hexdigest()
        with conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            print(f"User '{username}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting user: {e}")

def fetch_users(conn):
    """
    Fetch and display all users from the database securely.
    """
    try:
        with conn:
            cursor = conn.execute("SELECT id, username FROM users")
            for row in cursor.fetchall():
                print(f"User ID: {row[0]}, Username: {row[1]}")
    except sqlite3.Error as e:
        print(f"Error fetching users: {e}")

if __name__ == "__main__":
    db_name = "secure_app.db"
    conn = connect_to_database(db_name)
    
    if conn:
        create_table(conn)
        insert_user(conn, "secure_user", "secure_password123")
        fetch_users(conn)
        conn.close()
