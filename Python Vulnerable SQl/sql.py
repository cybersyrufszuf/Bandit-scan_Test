# Vulnerable Python code using raw SQL queries
import sqlite3

def get_user_data(username):
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    
    # UNSAFE: Directly embedding user input into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    connection.close()
    return result
    # Malicious input would now raise an error
    malicious_input = "http://169.254.169.254/latest/meta-data/"
    print(fetch_data(malicious_input))  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")


