#!/usr/bin/python3

"""script takes in an argument & displays all values
in the states table of hbtn_0e_0_usa where name matches the arg"""

import MySQLdb
import sys


def myfilter_states(username, password, database, state_name):
    """
    connects to the MySQL database and extracts username,
    password, database, and state_name
    """
    connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 passwd=password,
                                 db=database,
                                 port=3306)

    cursor = connection.cursor()

    sql_query = "SELECT DISTINCT * FROM states
    WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(sql_query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    """
    condition that checks the accurate number of args is provided
    """
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    myfilter_states(username, password, database, state_name)
