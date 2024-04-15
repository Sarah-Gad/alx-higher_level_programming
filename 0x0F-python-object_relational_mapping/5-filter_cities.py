#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
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
    newcurs = newcon.cursor()
    newcurs.execute(
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON cities.state_id=states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC", (sys.argv[4],)
            )
    thelist = list(newcurs.fetchall())
    print(", ".join([one[0] for one in thelist]))
    newcurs.close()
    newcon.close()


if __name__ == "__main__":
    main()
