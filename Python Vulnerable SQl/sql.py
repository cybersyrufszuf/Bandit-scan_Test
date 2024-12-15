import sqlite3
from flask import Flask, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return "Login successful"
    else:
        return "Login failed"




import hashlib
import os

# Vulnerable: Using MD5, a weak cryptographic hashing algorithm
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerable: Hardcoded secret key
SECRET_KEY = "1234567890abcdef"

# Vulnerable: Predictable random number generation
def generate_token():
    random_number = os.urandom(8)
    return hashlib.sha1(random_number).hexdigest()

# Example usage
if __name__ == "__main__":
    password = "password123"
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    token = generate_token()
    print(f"Generated Token: {token}")

if __name__ == '__main__':
    create_database()
    app.run(debug=True)


