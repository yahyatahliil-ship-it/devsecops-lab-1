import sqlite3

def get_user_data(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SECURE: Using parameterized queries prevents SQL injection
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_input,))
    return cursor.fetchall()
