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



import subprocess

# Vulnerable code: Command Injection
def execute_command(user_input):
    subprocess.run(f"echo {user_input}", shell=True)

# Test the function
execute_command("test; rm -rf /")
