#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as curseur:
        curseur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                        (argv[4],))
        rows = curseur.fetchall()
        for row in rows:
            print(row)
    curseur.close()
    db.close()
