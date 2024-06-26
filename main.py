import os
from clickhouse_driver import connect
from clickhouse_server import clickhouse
from sql_queries.create_tables import create_products, create_remainders
from sql_queries.select_queries import init_select_queries
from dotenv import load_dotenv
from logger import logger
from fake_data import create_data_for_product, create_data_for_remainders

load_dotenv()


def main(conn):
    cursor = conn.cursor()
    with conn.cursor() as cursor:
        clickhouse.create_table(cursor=cursor, sql_queries=create_products)
        clickhouse.create_table(cursor=cursor, sql_queries=create_remainders)
        products = create_data_for_product(10 ** 6)
        clickhouse.insert_data(cursor=cursor, table_name="products", data_dict=products)
        remainders = create_data_for_remainders(10 ** 6)
        clickhouse.insert_data(cursor=cursor, table_name="remainders", data_dict=remainders)



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
