#!/usr/bin/python3


import MySQLdb
from sys import argv


def main():
    """Lists a state in a database, securely."""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON states.id = cities.state_id")
    rows = cur.fetchall()
    for x in rows:
        print(x)

if __name__ == "__main__":
    main()
