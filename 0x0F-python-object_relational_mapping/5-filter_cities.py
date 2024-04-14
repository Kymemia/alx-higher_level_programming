#!/usr/bin/python3

"""script takes in the name of a state as an argument
and lists all cities of that state, using the DB hbtn_0e_4_usa"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """connects to MySQL & retrieves all the cities
    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database
        state_name (str): Name of state to filter cities
    Returns:
        None"""

    try:
        connection = MySQLdb.connect(host='localhost',
                                 user=username,
                                 passwd=password,
                                 db=database,
                                 port=3306)

        cursor = connection.cursor()

        sql_query = ("SELECT cities.id, cities.name FROM cities "
                     "JOIN states ON cities.state_id = states.id "
                     "WHERE states.name =%s ORDER BY cities.id ASC")

        cursor.execute(sql_query, (state_name,))
        cities = cursor.fetchall()

        for city in cities:
            print(city)

    except MySQLdb.Error as err:
        print({err})
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    """condition to check whether the correct number of args is present"""
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(username, password, database, state_name)
