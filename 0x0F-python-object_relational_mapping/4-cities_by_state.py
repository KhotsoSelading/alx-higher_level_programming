#!/usr/bin/python3
"""Lists all cities by state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    db_cur = db_conn.cursor()
    db_cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """)
    query_rows = db_cur.fetchall()
    for row in query_rows:
        print(row)
    db_cur.close()
    db_conn.close()
