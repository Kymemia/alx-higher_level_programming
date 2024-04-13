#!/usr/bin/python3

"""Script takes in arguments & displays
the values in the states table of hbtn_0e_0-usa
where name marches the arg.
script is safe from MySQL injections"""


import MySQLdb
import sys


def my_safe_filter(username, password, database, state_name):
    """connects to MySQL & retrieves username
    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database
        state_name (str): Name to be searched for
    Returns:
        None"""

    connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 passwd=password,
                                 db=database,
                                 port=3306)

    cursor = connection.cursor()

    sql_query = ("SELECT * FROM states WHERE name = %s "
                 "ORDER BY id ASC")

    cursor.execute(sql_query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    """checks if the correct number of args is provided"""
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    my_safe_filter(username, password, database, state_name)
