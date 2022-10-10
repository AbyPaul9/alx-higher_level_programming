#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys


def main():
    """
        takes in an argument and displays all values in the states
        table of hbtn_0e_0_usa where name matches the argument.
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
    stName = sys.argv[4]
    req = "SELECT *  FROM states WHERE BINARY name='{}'\
         ORDER BY id ASC".format(sys.argv[4])
    cur.execute(req)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
