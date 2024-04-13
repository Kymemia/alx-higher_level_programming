#!/usr/bin/python3

"""script lists all cities from the database, hbtn_0e_4_usa"""


import MySQLdb
import sys


def cities_b_states(username, password, database):
    """connects to MySWL database and retrieves all cities
    Args:
        username (str): MySQL username
        passwrod (str): MySQL password
        database (str): MySQL database name
    Returns:
        None"""

    connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 passwd=password,
                                 db=database,
                                 port=3306)

    cursor = connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "ORDER BY id ASC")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    """condition that checks the adequate number of args is present"""
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    cities_b_states(username, password, database)
