#!/usr/bin/python3
"""
This script displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
            "SELECT * FROM `states` WHERE BINARY `name` = '{}'"
            "ORDER BY `id` ASC".format(sys.argv[4]))
    for row in newcurs:
        print(row)
    newcurs.close()
    newcon.close()


if __name__ == "__main__":
    main()
