#!/usr/bin/python3
"""
This script lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


def main():
    newcon = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    newcur = newcon.cursor()
    newcur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for row in newcur:
        print(row)
    newcur.close()
    newcon.close()


if __name__ == "__main__":
    main()
