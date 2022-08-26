import sqlite3


def database(db):
    return sqlite3.connect(db)


def insert(vcon, vsql):
    connection = vcon
    connection.cursor()
    connection.execute(vsql)
    connection.commit()