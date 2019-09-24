import MySQLdb

try:
    connection = MySQLdb.connect (host = "localhost",
                             user = "root",
                             passwd = "sql123$",
                             db = "mysql")
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee") 
print('''Result of "SELECT * FROM employee":''')
result = cursor.fetchall() 
for r in result:
    print(r)

cursor.close()
connection.close()