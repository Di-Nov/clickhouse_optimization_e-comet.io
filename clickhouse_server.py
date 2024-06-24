from datetime import date


class WorkWithClickhouse:
    def create_table(self, cursor, sql_queries):
        cursor.execute(sql_queries)
        cursor.fetchall()

    def insert_data(self, cursor, table_name, data_dict=None):
        match table_name:
            case "products":
                x = [{'product_id': 123, 'product_name': "test1", 'brand_id': 123, 'seller_id': 1235,
                      'updated': date.today()},
                     {'product_id': 124, 'product_name': "test1", 'brand_id': 124, 'seller_id': 1236,
                      'updated': date.today()}]
                cursor.executemany(f'INSERT INTO {table_name} (*) VALUES', x)

            case "remainders":
                pass

    def select_data(self, cursor, sql_queries):
        pass


clickhouse = WorkWithClickhouse()

