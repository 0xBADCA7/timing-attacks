import sqlite3

conn = sqlite3.connect('/tmp/sample.db')
c = conn.cursor()

# Create a dummy table
c.execute('''CREATE TABLE users (int id IDENTITY, username text(40), password text(128)) ''')

# Insert the same "secret" that we have wired-in in index.py
c.execute('''INSERT INTO users VALUES (1, 'admin', 'fad08d06495532c3ae5db5209834956b0114da77')''')
conn.commit()
conn.close()
