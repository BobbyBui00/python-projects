import pandas as pd
import non_async_requests
import async_requests
from pandas import DataFrame
from sqlalchemy import create_engine
import asyncio
import json

def main():
    # engine = create_engine('mysql')
    engine = init_db('postgresql')
    df = pd.DataFrame()
    json_data = non_async_requests.main(True)
    # json_data = async_requests.main(True)
    for i in range(len(json_data)):
        print(json_data[i])
        df = pd.concat([df, pd.DataFrame([json_data[i]])], ignore_index=True)

    df.to_sql(name='transactions', con=engine, if_exists='append', index=False)


def init_db(db_type):
    # db_config = get_db_env(db_type)
    db_config = get_db_config(db_type)
    return create_engine(f'{db_type}://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}@{db_config["DB_HOST"]}:{db_config["DB_PORT"]}/{db_config["DB_NAME"]}')


def get_db_env(db_type):
    import os

    if db_type == 'postgresql' or db_type == 'mysql':
        return {
            'DB_HOST': os.getenv(f'{db_type.upper()}_DB_HOST'),
            'DB_PORT': os.getenv(f'{db_type.upper()}_DB_PORT'),
            'DB_NAME': os.getenv(f'{db_type.upper()}_DB_NAME'),
            'DB_USER': os.getenv(f'{db_type.upper()}_DB_USER'),
            'DB_PASSWORD': os.getenv(f'{db_type.upper()}_DB_PASSWORD'),
        }
    else:
        raise Exception('Unknown database type')

def get_db_config(db_type):
    import configparser

    config = configparser.ConfigParser()

    if db_type == 'postgresql' or db_type == 'mysql':
        config.read('../resources/config.ini')
        return {
            'DB_HOST': config[f'{db_type}']['host'],
            'DB_PORT': config[f'{db_type}']['port'],
            'DB_NAME': config[f'{db_type}']['database_name'],
            'DB_USER': config[f'{db_type}']['user'],
            'DB_PASSWORD': config[f'{db_type}']['password'],
        }
    else:
        raise Exception('Unknown database type')

if __name__ == '__main__':
    main()