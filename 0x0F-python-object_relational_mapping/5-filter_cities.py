#!/usr/bin/python3


import MySQLdb
from sys import argv


def main():
    """Lists all cities in a state in a database, securely."""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    lizt = []

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ", [state])
    rows = cur.fetchall()
    for x in rows:
        for y in x:
            lizt.append(y)
    print(', '.join(lizt))

if __name__ == "__main__":
    main()
