import sqlalchemy
from sqlalchemy.orm import sessionmaker
import configparser


def insert_into_table(_dicts, table):
    values = [table(**_dict) for _dict in _dicts]
    insert_into_db(values)


def get_db_credentials():
    environ = configparser.ConfigParser()
    filename = 'environment.ini'
    environ.read(filename)
    host = environ['mysql']['host']
    user = environ['mysql']['user']
    password = environ['mysql']['password']
    return host, user, password


def create_db_engine():
    host, user, password = get_db_credentials()
    return sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}', pool_recycle=1800)


def create_db_session():
    engine = create_db_engine()
    _session = sessionmaker(engine)
    return _session()


def insert_into_db(values):
    with create_db_session() as session:
        session.bulk_save_objects(values)
        session.commit()
