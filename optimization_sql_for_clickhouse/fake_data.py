from faker import Faker
from datetime import date, timedelta

fake_data = Faker()


def create_data_for_product(count):
    data_products = [
        {
            'product_id': fake_data.random_int(min=1, max=10**7),
            'product_name': fake_data.company(),
            'brand_id': fake_data.random_int(min=1, max=10 ** 3),
            'seller_id': fake_data.random_int(min=1, max=10 ** 3),
            'updated': fake_data.date_between(
                start_date=date.today() - timedelta(days=5),
                end_date=date.today() + timedelta(days=1))
        } for _ in range(count)]
    return data_products


def create_data_for_remainders(count):
    data_remainders = (
        {
            'date': fake_data.date_between(
                start_date=date.today() - timedelta(days=30),
                end_date=date.today() + timedelta(days=1)),
            'product_id': fake_data.random_int(min=1, max=1000),
            'remainder': fake_data.random_int(min=1, max=1_000),
            'price': fake_data.random_int(min=1, max=1_000),
            'discount': fake_data.random_int(min=1, max=100),
            'pics': fake_data.random_int(min=1, max=100),
            'rating': fake_data.random_int(min=1, max=100),
            'reviews': fake_data.random_int(min=1, max=100),
            'new': fake_data.boolean()
        } for _ in range(count))
    return data_remainders
