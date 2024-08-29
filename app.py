import pandas as pd
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, select

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

    select_all_query = select(test_table)
    select_all_results = conn.execute(select_all_query)

    for row in select_all_results.fetchall():
        output_row="ID: "+str(row[0])+"\tName: "+row[1]+"\tAge: "+str(row[2])+"\tDepartment: "+row[3]
        print (output_row)
