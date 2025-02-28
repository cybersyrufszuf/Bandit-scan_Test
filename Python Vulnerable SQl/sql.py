import sqlite3

# Establishing connection to a test database
connection = sqlite3.connect("test.db")
cursor = connection.cursor()

# Creating a sample users table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
connection.commit()

# Vulnerable function
def authenticate_user(username, password):
    # This query is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # Debugging purpose only
    cursor.execute(query)
    return cursor.fetchone()

# Example input that can exploit the vulnerability
user_input_username = "admin' OR '1'='1"
user_input_password = "does_not_matter"

# Attempt to authenticate with malicious input
user = authenticate_user(user_input_username, user_input_password)
if user:
    print("Login successful:", user)
else:
    print("Login failed")

connection.close()
