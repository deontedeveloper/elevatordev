# Demo program to show SQL examples
# https://dev.mysql.com/doc/connector-python/en/
# Install the MySQL connector library on your RPi
# sudo  pip install mysql-connector-python
# Copy this program to your personal repo
# Change all instances of customers to your actual name

import mysql.connector

# Create a connection object to the RDMS on Winhost.com
# If running on a local or local server instance of MySQL, you would run commands to create a database first
#   The command would be CREATE DATABASE customers
"""
mydb = mysql.connector.connect(
	host="my03.winhost.com",
	database='mysql_24101_sdev265',
	user="sdev265",
	passwd="sdev265$")
"""
mydb = mysql.connector.connect(
	host="10.81.104.8",
	database='sdev265',
	user="sdev265",
	passwd="sdev265$")

mycursor = mydb.cursor()	# A cursor is a temporary work area in memory
"""
sql = "DROP TABLE IF EXISTS employees;"
mycursor.execute(sql)

sql = " DROP TABLE IF EXISTS customers;"
mycursor.execute(sql)

sql = " DROP TABLE IF EXISTS books1_tbl;"
mycursor.execute(sql)
"""
print('Create a table named customers with 2 fields (attributes)')
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

print ('Get list of tables in the database\n')
mycursor.execute("SHOW TABLES")

print ('Showing list of tables\n')
for x in mycursor:
	print(x)
	
print ('Inserting a record in table\n')
sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
val = ('Fred', 'Route 6640')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

print ('Inserting a record in table method 2 \n')
# sql = "INSERT INTO customers (name, address) VALUES ('Sally', '456 Elm Street')"
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ('Sally', '456 Elm Street')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

print ('Showing records in table using SQL select statement \n')
mycursor.execute("SELECT * FROM customers ORDER BY name")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
	print(x[1])

print ('Change (update) a records \n')
sql = "UPDATE customers SET address = '123 Main Street' WHERE address = 'Route 6640';"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
	
print ('\nshowing records ordered by name')
mycursor.execute("SELECT * FROM customers order by name;")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
	#print(x[1])

print ('\n Delete a record')
sql = "DELETE FROM customers WHERE name = 'fred';"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

print ('show records after delete \n')
mycursor.execute("SELECT * FROM customers order by name;")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
	#print(x[1])
print ('Delete customer table if it exists \n')
sql = "DROP TABLE IF EXISTS employees;"
mycursor.execute(sql)
	
print ('Create an example of a complex table \n')

sql = (   "CREATE TABLE employees ("
" emp_no int(11) NOT NULL AUTO_INCREMENT,"
" birth_date date NOT NULL,"
" first_name varchar(14) NOT NULL,"
" last_name varchar(16) NOT NULL,"
" gender enum('M','F') NOT NULL,"
" hire_date date NOT NULL,"
" PRIMARY KEY (emp_no))"   )
print (sql + '\n\n')
mycursor.execute(sql)

sql = (   "CREATE TABLE IF NOT EXISTS LiftLog ("
" id int(11) NOT NULL AUTO_INCREMENT,"
" eventDate date NOT NULL,"
" category varchar(30) NOT NULL,"
" description text NOT NULL,"
" PRIMARY KEY (id))"   )
print (sql + '\n\n')
mycursor.execute(sql)

print ('Show tables after adding new table \n')
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

mycursor.close()


