import psycopg2


class DBManager:
    def __init__(self, table):
        self.table = table
        self.conn = psycopg2.connect(
            dbname="job_database",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )


    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cur:
            cur.execute(
                f'''SELECT employer, COUNT(name) AS total FROM {self.table}
                        GROUP BY employer
                        ORDER BY total DESC'''
            )
            rows = cur.fetchall()
            print(f"Company name -- number of vacancies")
            for row in rows:
                employer, total = row
                print(f"{employer} -- {total}")

    def get_all_vacancies(self):
        with self.conn.cursor() as cur:
            cur.execute(
                f'''SELECT employer, name, salary_from, currency FROM {self.table}'''
            )
            rows = cur.fetchall()
            print(f"Company name -- vacancy name -- salary from -- currency")
            for row in rows:
                employer, name, salary_from, currency = row
                print(f"{employer} -- {name} -- {salary_from} -- {currency}")


    def get_avg_salary(self):
        with self.conn.cursor() as cur:
            cur.execute(
                f'''SELECT AVG(salary_from) FROM {self.table}'''
            )
            rows = cur.fetchone()
            for row in rows:
                avg_salary = float(row)
                print(f"Average salary -- {round(avg_salary)}")
    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cur:
            cur.execute(
                f"""SELECT employer, name, salary_from, currency 
                FROM {self.table} WHERE salary_from > (SELECT AVG(salary_from) FROM {self.table}) 
                ORDER BY salary_from DESC"""
            )
            rows = cur.fetchall()
            print("List of vacancies with above average salaries.")
            print(f"Company name -- vacancy name -- salary from -- currency")
            for row in rows:
                employer, name, salary_from, currency,  = row
                print(f"{employer} -- {name} -- {salary_from} -- {currency}")


    def get_vacancies_with_keyword(self, keyword):
        # курьер
        with self.conn.cursor() as cur:
            cur.execute(
                f"""SELECT name, salary_from, currency, employer 
                FROM {self.table} WHERE name LIKE '%{keyword}%'"""
            )
            rows = cur.fetchall()
            if cur.rowcount == 0:
                print("There are no such positions.")
            else:
                print('A list of vacancies matching your keyword:\n')
                for row in rows:
                    name, salary_from, currency, employer = row
                    print(f"{name} -- {salary_from}- - {currency} -- {employer}")


