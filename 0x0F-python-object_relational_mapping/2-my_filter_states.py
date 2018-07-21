#!/usr/bin/python3


import MySQLdb
from sys import argv


def main():
    """Lists a state in a database."""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'".
                format(searched))

    print(cur.fetchall()[0])

    db.close()
    cur.close()

if __name__ == "__main__":
    main()
