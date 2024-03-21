#!/usr/bin/python3
"""
This script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument
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

    cursor = db.cursor()
    cursor.execute("SELECT `id`, `name` \
                    FROM `states` \
                    WHERE `name` LIKE BINARY '{}' \
                    ORDER BY states.id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
