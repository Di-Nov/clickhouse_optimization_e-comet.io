from datetime import date
from faker import Faker


class WorkWithClickhouse:

    def create_table(self, cursor, sql_queries):
        cursor.execute(sql_queries)
        cursor.fetchall()

    def insert_data(self, cursor, table_name, data_dict=None):
        match table_name:
            case "products":
                cursor.executemany(f'INSERT INTO {table_name} (*) VALUES', data_dict)

            case "remainders":
                pass

    def select_data(self, cursor, sql_queries):
        cursor.execute(sql_queries)
        x = cursor.fetchall()
        print(x)


clickhouse = WorkWithClickhouse()
