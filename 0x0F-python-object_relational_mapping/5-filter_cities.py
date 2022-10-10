#!/usr/bin/python3
"""
    script that lists all cities of that state,
    using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def main():
    """
        lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT 1 AS a,\
        GROUP_CONCAT(c.name ORDER BY c.id ASC SEPARATOR ', ')\
            AS cities_name FROM cities c INNER JOIN states s\
                ON s.id = c.state_id WHERE s.name = %s\
                    ORDER BY c.id ASC ", (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] is None:
            print()
        else:
            print(row[1])
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
