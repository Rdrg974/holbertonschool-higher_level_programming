#!/usr/bin/python3
"""
This script that lists all states with a name
starting with N from the database hbtn_0e_0_usa
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
                    WHERE `name` LIKE BINARY 'N%' \
                    ORDER BY `id` ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
