import psycopg2


def create_database():
    """
    Create database.
    :return:
    """
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("CREATE DATABASE job_database")

    cur.close()
    conn.close()
