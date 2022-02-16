import MySQLdb

cn = MySQLdb.connect(user='root')
cn.query('CREATE DATABASE test') #Creating database
cn = MySQLdb.connect(db='test') #Selecting database
cur = cn.cursor() #Creating cursor object
cur.execute('CREATE TABLE users(login VARCHAR(8), uid INT)') #Create table

# Next we will insert a few rows into the database
cur.execute("INSERT INTO users VALUES('Arun', 7000)")
cur.execute("INSERT INTO users VALUES('Arjun', 7001)")
cur.execute("INSERT INTO users VALUES('Aditya', 7200)")
cur.execute("SELECT * FROM users")

for data in cur.fetchall():
  print('%s\t%s' % data)

  
'''Arun 7000
Arjun 7001
Aditya 7200'''

cur.execute("UPDATE users SET login='Arjuna2' WHERE uid=7001")
cur.execute("SELECT * FROM users")
for data in cur.fetchall():
  print('%s\t%s' % data)

  
'''Arun 7000
Arjun 7001
Aditya 7200'''

cur.execute('DELETE FROM users WHERE login="Arjuna2"')
cur.execute('DROP TABLE users')
cur.close()
cn.commit()
cn.close()
