import pandas as pd
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, select


# def process_data(engine):
#     conn = engine.connect()

#     data = pd.read_sql('Select min(age), max(age) from test_table Where length(name)<6', conn)

#     return data

# def create_table(engine):
#     conn=engine.connect()








if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'test_db'

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    conn = engine.connect()
    metadata = MetaData()

    test_table=Table('test_table', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('department', String))

    metadata.create_all(engine)

    insertion_query = test_table.insert().values([
        {'name':'Alice', 'age':30, 'department':'HR'},
        {'name':'Bob', 'age':25, 'department':'Engineering'},
        {'name':'Charlie', 'age':35, 'department':'Sales'}
    ])

    conn.execute(insertion_query)

    conn.commit()

    print("im here")

    select_all_query = select(test_table)
    select_all_results = conn.execute(select_all_query)

    print(select_all_results.fetchall())





    



    # result = process_data(engine)

    # print("Максимальное и минимальное значения возраста:")
    # print(result)