import sqlite3

def get_user_data(user_input):
  conn = sqlite3.connect("user.db")
cursor = conn.cursor() 
# secure: using parameterized quries prevents sql injection 
query = "select * from users where id = ?"
cursor.execute(query, (user_input,))
return cursor.fetchall()
