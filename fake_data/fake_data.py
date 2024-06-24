# from faker import Faker
#
# faker = Faker()
#
# self.persons = [
#             PersonSchema(
#                 id=self.fake.uuid4(),
#                 name=self.fake.name(),
#                 role=random.choice(list(ROLES.values())))
#             for _ in range(PERSONS_QTY)
#         ]
#
# self.genres = [GenreSchema(id=self.fake.uuid4(), name=name) for name in genres]
#
# self.items = [FilmWorkSchema(
#             id=self.fake.uuid4(),
#             imdb_rating=round(random.uniform(RATING_MIN, RATING_MAX), NUMBER_OF_DECIMALS),
#             genre=random.sample(self.genres, k=random.randint(1, 3)),
#             title=self.fake.bs().title(),
#             persons=random.sample(self.persons, k=random.randint(5, 15)),
#             description=self.fake.text(),
#         ) for _ in range(FILMS_QTY)]
#
