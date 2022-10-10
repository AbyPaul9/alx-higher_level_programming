#!/usr/bin/python3
"""
    script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


def main():
    """
        lists all states with a name starting with N (upper N)
        from the database hbtn_0e_0_usa
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
    req = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(req)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
