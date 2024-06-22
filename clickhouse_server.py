import pyarrow as pa


class WorkWithClickhouse:
    def create_table(self, client, sql_queries):
        client.execute(
            sql_queries,
        )

    def import_data(self, client, sql_queries):
        # Import a table
        table = pa.Table.from_pydict(
            {
                "col1": [1, 2, 3],
                "col2": ["a", "b", "d"],
            },
        )
        client.insert("test", table)

    def read_table(self, client, sql_queries):
        # Read into a table
        table = client.read_table("SELECT * FROM test")
        print(table)


clickhouse = WorkWithClickhouse()

# def read_iterator_of_batches(self, client, sql_queries):
#     # Read iterator of batches
#     batches = client.read_batches("SELECT * FROM test")
#     for batch in batches:
#         print(batch)

# # Use query parameters
# table = client.read_table(
#     """
#     SELECT * FROM test
#     WHERE col1 = {value:Int64}
#     """,
#     params={"value": 2},
# )
# print(table)
#
# # Use query settings
# table = client.read_table(
#     "SELECT col2 FROM test",
#     settings={"output_format_arrow_string_as_string": 1},
# )
# print(table["col2"])
