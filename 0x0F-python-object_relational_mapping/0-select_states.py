#!/usr/bin/python3
"""Lists all states from a database."""


import MySQLdb
from sys import argv


username = argv[1]
password = argv[2]
database = argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=username,
						passwd=password, db=database)
cur = db.cursor()
cur.execute("SELECT * FROM states".format(database))
rows = cur.fetchall()
for x in rows:
	print(x)
