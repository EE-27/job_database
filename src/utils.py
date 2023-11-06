import json

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


def create_table():
    conn = psycopg2.connect(
        dbname="job_database",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS table1 
    (
        id INT PRIMARY KEY,
        name TEXT,
        employer TEXT,
        salary_from REAL,
        salary_to REAL,
        currency VARCHAR(3),
        requirement TEXT,
        responsibility TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_values():
    conn = psycopg2.connect(
        dbname="job_database",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    with open("json.json", "r", encoding='utf-8') as json_file:
        json_data = json_file.readlines()
        for line in json_data:
            item = json.loads(line)
            empl_id = item["id"]
            name = item["name"]
            employer = item["employer"]["name"]

            if "salary" in item and item["salary"]:
                salary_from = item["salary"]["from"]
                salary_to = item["salary"]["to"]
                salary_currency = item["salary"]["currency"]
            else:
                salary_from = None
                salary_to = None
                salary_currency = None

            requirement = item['snippet']['requirement']
            responsibility = item['snippet']['responsibility']

            insert_query = """
                INSERT INTO table1 (id, name, employer, salary_from, salary_to, currency, requirement, responsibility)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            data = (empl_id, name, employer, salary_from, salary_to, salary_currency, requirement, responsibility)
            cur.execute(insert_query, data)
    conn.commit()
    conn.close()

# insert_values()