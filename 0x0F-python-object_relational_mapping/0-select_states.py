#!/usr/bin/python3
"""Lists of all states"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    try:
        db_conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                                  passwd=password, db=database_name)
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if db_conn:
            db_conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
