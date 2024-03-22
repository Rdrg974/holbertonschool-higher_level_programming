#!/usr/bin/python3
"""
This script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as curseur:
        curseur.execute("SELECT cities.id, cities.name, states.name\
                        FROM cities\
                        JOIN states ON cities.state_id = states.id\
                        ORDER BY cities.id ASC")
        rows = curseur.fetchall()
        for row in rows:
            print(row)
    curseur.close()
    db.close()
