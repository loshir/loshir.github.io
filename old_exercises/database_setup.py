import sqlite3

con = sqlite3.connect("telegram_messages.db")
cur =con.cursor()

try:
	cur.execute("CREATE TABLE messages(id, date, name, content)")
except:
	""