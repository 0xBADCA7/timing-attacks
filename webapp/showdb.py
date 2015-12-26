import sqlite3

conn = sqlite3.connect('/tmp/sample.db')
c = conn.cursor()
r = c.execute('''SELECT password FROM users WHERE username = 'admin' ''')
print(c.fetchone())
conn.commit()
conn.close()