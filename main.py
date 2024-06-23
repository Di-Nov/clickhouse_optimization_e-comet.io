import os
import clickhouse_arrow as ch
from dotenv import load_dotenv

from logger import logger

from clickhouse_server import clickhouse
from sql_queries.create_tables import create_products, create_remainders

load_dotenv()

#
def main(client_clickhouse):
    clickhouse.create_table(client=client_clickhouse, sql_queries=create_products)
    clickhouse.create_table(client=client_clickhouse, sql_queries=create_remainders)


if __name__ == '__main__':
    try:
        with ch.Client(f"http://{os.getenv('CLICKHOUSE_HOST')}:{os.getenv('CLICKHOUSE_PORT')}",
                       password=os.getenv('CLICKHOUSE_PASSWORD')) as client:
            main(client_clickhouse=client)
    except Exception as ex:
        logger.error(ex)
    finally:
        logger.info("Script the end")
