
import os
import psycopg2


def db_init():
    """ Connect to the PostgreSQL database server """

    connection = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
        "DB_NAME"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
    cur = connection.cursor()
    print("#################### connection established #######################")
    queries = create_tables()
    try:
        for query in queries:
            cur.execute(query)
            connection.commit()
        connection.close()
    except psycopg2.DatabaseError as error:
        print(error)


def create_tables():
    create_user_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR (200) NOT NULL UNIQUE,
        firstname VARCHAR (200) NOT NULL,
        lastname VARCHAR (200) NOT NULL,
        othername VARCHAR (200),
        phone VARCHAR (200) NOT NULL,
        email VARCHAR (200) NOT NULL UNIQUE,
        password VARCHAR (200) NOT NULL,
        passportUrl VARCHAR (200),
        isPolitician BOOLEAN,
        isAdmin BOOLEAN
    )"""

    create_party_table = """
    CREATE TABLE IF NOT EXISTS parties (
        id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL UNIQUE,
        hqAddress VARCHAR (200),
        logoUrl VARCHAR
    )
    """
    create_office_table = """
    CREATE TABLE IF NOT EXISTS offices (
        id SERIAL PRIMARY KEY,
        name VARCHAR(200) NOT NULL UNIQUE,
        type VARCHAR (200)
    )
    """
    create_vote_table = """
    CREATE TABLE IF NOT EXISTS votes (
        id SERIAL PRIMARY KEY,
        createdOn DATE,
        type VARCHAR (200),
        createdBy INTEGER NOT NULL,
        office INTEGER NOT NULL,
        candidate INTEGER NOT NULL
    )
    """
    create_candidate_table = """
    CREATE TABLE IF NOT EXISTS candidates (
        id SERIAL PRIMARY KEY,
        office INTEGER NOT NULL,
        party INTEGER NOT NULL,
        candidate INTEGER NOT NULL
    )
    """
    queries = [create_user_table, create_vote_table,
               create_candidate_table, create_party_table, create_office_table]
    return queries


def delete_tables():
    delete_party = """
    DROP TABLE IF EXISTS parties CASCADE
    """
    delete_user = """
    DROP TABLE IF EXISTS users CASCADE
    """
    delete_votes = """
    DROP TABLE IF EXISTS votes CASCADE
    """
    delete_candidates = """
    DROP TABLE IF EXISTS  candidates CASCADE
    """
    queries = [delete_user, delete_party, delete_votes, delete_candidates]
    return queries


def tear_down():
    connection = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
        "DB_NAME"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
    cursor = connection.cursor()
    for query in delete_tables():
        cursor.execute(query)
        connection.commit()
    connection.close()


def db_connection():
    connection = psycopg2.connect(host=os.environ.get("DB_HOST"), database=os.environ.get(
        "DB_NAME"), user=os.environ.get("DB_USER"), password=os.environ.get("DB_PASSWORD"))
    return connection


if __name__ == "__main__":
    db_init()
