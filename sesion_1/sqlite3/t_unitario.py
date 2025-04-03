import sqlite3 as sql

path = "sqlite3/user.db"

conex = sql.connect(path)
cursor = conex.cursor()

# cursor.execute("ALTER TABLE users RENAME nombre TO name;")

# cursor.execute("UPDATE users SET id = 10 WHERE id = 12;")

# cursor.execute("DELETE FROM users WHERE id = 13;")

# cursor.execute(""" CREATE TABLE users (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             nombre TEXT( 50) NOT NULL,
#             age INTEGER NOT NULL,
#             country TEXT (50),
#             email TEXT (100) NOT NULL
            
#     ); """)



conex.commit()
conex.close()