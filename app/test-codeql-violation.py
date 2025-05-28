import sqlite3

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    # Vulnerable SQL query (SQL injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = conn.execute(query)
    return result.fetchone()