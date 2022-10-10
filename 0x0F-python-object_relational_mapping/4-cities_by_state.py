#!/usr/bin/python3
"""
    script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def main():
    """
        lists all cities from the database hbtn_0e_4_usa
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
        FROM cities c\
            INNER JOIN states s ON s.id = c.state_id\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
