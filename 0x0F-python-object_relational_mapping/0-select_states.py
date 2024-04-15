#!/usr/bin/python3

import sys
import MySQLdb

def main():
    newcon = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    newcurs = newcon.cursor()
    newcurs.execute(f"SELECT * FROM `states` ORDER BY `id` ASC")
    for row in newcurs:
        print(row)
    newcurs.close()
    newcon.close()

if __name__ == "__main__":
    main()

