#!/usr/bin/python3
"""Lists all states starting with passed arg, prevents injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                              user=argv[1], passwd=argv[2], db=argv[3])
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(argv[4]))
    rows = db_cur.fetchall()
    for row in rows:
        print(row)
    db_cur.close()
    db_conn.close()
