import sqlite3

cn = sqlite3.connect('sqlite_test/test')
cur = cn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8), uid INTEGER)')
cur.execute('INSERT INTO users VALUES("Arun", 100)')
cur.execute('INSERT INTO users VALUES("Arjun", 110)')
cur.execute('SELECT * FROM users')


for eachUser in cur.fetchall():
    print(eachUser)

    
cur.execute('DROP TABLE users')
cur.close()
cn.commit()
cn.close()
