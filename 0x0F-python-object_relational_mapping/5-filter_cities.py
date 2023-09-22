#!/usr/bin/python3
"""Lists all cities by state passed by user"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                              user=argv[1], passwd=argv[2], db=argv[3])
    db_cur = db_conn.cursor()
    db_cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """, (argv[4],))
    query_rows = db_cur.fetchall()
    print(", ".join([row[1] for row in query_rows]))
    db_cur.close()
    db_conn.close()
