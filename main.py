import sqlite3

connection= sqlite3.connect("database.sl3" , 5)
cur = connection.cursor()

#cur.execute("ctrate table users (id int primary kay not null , login text, password text);")
#cur.execute("indert into users (id, login, password) values (2, 'leo', 'admin');")
#cur.execute("indert into users (id, login, password) values (2, 'leo', 'admin');")
#cur.execute("indert into users (id, login, password) values (2, 'leo', 'admin');")
#cur.execute("indert into users (id, login, password) values (2, 'leo', 'admin');")
#cur.execute("indert into users (id, login, password) values (2, 'leo', 'admin');")
cur.execute("select password from users where login='leo';")
connection.commit()
res = cur.fetchall()
print(res)

#print(connection)
#print(cur)

connection.close()