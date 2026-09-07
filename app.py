import sqlite3 

def get-user-data (user_input): 
conn = sqlite3.connect ("users.db")
cursor = conn.cursor()
# vulnerable SQL INJECTION QUERY 
query = select * from users where id = '" + user_input + "'"
cursor.execute(query)
return cursor.fetchall()
