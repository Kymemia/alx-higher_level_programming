#!/usr/bin/python3

"""script takes in the name of a state as an argument
and lists all cities of that state, using the DB hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306
                         )

    cursor = db.cursor()

    sql = """SELECT cities.name FROM states
             INNER JOIN cities ON states.id = cities.state_id
             WHERE states.name = %(state_name)s
             ORDER BY cities.id ASC"""

    cursor.execute(sql, {'state_name': sys.argv[4]})
    data = cursor.fetchall()

    print(", ".join([city[0] for city in data]))

    cursor.close()
    db.close()
