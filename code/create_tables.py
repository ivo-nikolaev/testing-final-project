import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text, email text, token text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS photos (id INTEGER PRIMARY KEY AUTOINCREMENT, photo_name text, data BLOB, visible BOOLEAN, user_id INTEGER, CONSTRAINT fk_user_ids FOREIGN KEY (user_id) REFERENCES user(id))"
cursor.execute(create_table)

connection.commit()

connection.close()