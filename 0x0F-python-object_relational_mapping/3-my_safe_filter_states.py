#!/usr/bin/python3
"""
    script that takes in arguments and displays all values in the states table\
    of hbtn_0e_0_usa where name matches the argument. But this time,\
    write one that is safe from MySQL injections!
"""


import MySQLdb
import sys


def main():
    """
        takes in arguments and displays all values in the states table\
        of hbtn_0e_0_usa where name matches the argument. But this time,\
        write one that is safe from MySQL injections!
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
    cur.execute("SELECT *\
        FROM states\
            WHERE name=%(stateName)s\
                ORDER BY id ASC", {'stateName': sys.argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
