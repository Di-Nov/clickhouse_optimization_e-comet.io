from faker import Faker
import faker_commerce
from datetime import date

fake_data = Faker()


def data_for_product(count):
    data_products = [
        {'product_id': fake_data.random_int(min=1, max=10 ** 3), 'product_name': fake_data.company(),
         'brand_id': fake_data.random_int(min=1, max=10 ** 3), 'seller_id': fake_data.random_int(),
         'updated': fake_data.date_between(start_date=date(2020, 7, 14), end_date=date.today())} for _ in range(count)]
    return data_products

