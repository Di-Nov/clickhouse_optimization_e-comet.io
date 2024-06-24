import os
from clickhouse_driver import connect
from clickhouse_server import clickhouse
from sql_queries.create_tables import create_products, create_remainders
from dotenv import load_dotenv
from logger import logger

load_dotenv()


#
def main(conn):
    cursor = conn.cursor()
    with conn.cursor() as cursor:
        clickhouse.create_table(cursor=cursor, sql_queries=create_products)
        clickhouse.create_table(cursor=cursor, sql_queries=create_remainders)

        clickhouse.insert_data(cursor=cursor, table_name="products")
        # print(cursor.rowcount())


if __name__ == '__main__':
    try:
        with connect(host=os.getenv('CLICKHOUSE_HOST'), port=os.getenv('CLICKHOUSE_PORT'),
                     password=os.getenv('CLICKHOUSE_PASSWORD')) as connect_clickhouse:
            main(connect_clickhouse)
    except Exception as ex:
        logger.error(ex)
    finally:
        connect_clickhouse.close()
        logger.info("connect closed")
