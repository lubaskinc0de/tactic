from sqlalchemy import MetaData, Table, Column, BigInteger

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("user_id", BigInteger, primary_key=True),
)
