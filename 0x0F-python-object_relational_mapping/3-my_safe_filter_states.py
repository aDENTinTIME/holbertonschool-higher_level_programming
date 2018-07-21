#!/usr/bin/python3


import MySQLdb
from sys import argv


def main():
    """Lists a state in a database, securely."""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", [searched])
    rows = cur.fetchall()
    for x in rows:
        print(x)

if __name__ == "__main__":
    main()
