#!/usr/bin/python3
"""Lists of all states"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                              user=argv[1], passwd=argv[2], db=argv[3])
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = db_cur.fetchall()
    for row in query_rows:
        print(row)
    db_cur.close()
    db_conn.close()
