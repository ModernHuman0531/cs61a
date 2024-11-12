import sqlite3
# To construct a connection i pass in the name of a database file.
# Create a sql object and give a connection to n.db
db = sqlite3.Connection("n.db") #n.db is the database name
# object sql have execute() method that can execute sql code with ""
db.execute("create table nums as Select 2 union select 3;")
# We can use python expression to give values in sql
db.execute("insert into nums values(?), (?), (?);", range(4, 7))
# fetchall() method will fetch the contents of resultic table as a list of tuple
# Means represnt the table as tuple.
print(db.execute("select * from nums;").fetchall())
# use commit method to let the n.db file
# contain all the content in the database
db.commit()