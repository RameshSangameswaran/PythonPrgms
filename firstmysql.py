import MySQLdb

connection = MySQLdb.connect (host = "localhost",
                              user = "root",
                              passwd = "sql123$",
                              db = "mysql")

cursor = connection.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print("server version:", row[0])
cursor.close()
connection.close()