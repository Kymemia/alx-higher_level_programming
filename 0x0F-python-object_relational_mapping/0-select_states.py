#!/usr/bin/python3

"""script that lists all states from the DB, hbtn_0e_usa"""


import MySQLdb
import sys


def list_states(username, password, database):
    """connects to the MySQL database and extracts username,
    password, and database"""

    connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 passwd=password,
                                 db=database,
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    """condition that checks the accurate number of args is provided"""
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
