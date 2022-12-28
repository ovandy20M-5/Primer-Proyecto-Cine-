import psycopg2
from psycopg2 import DatabaseError
from decouple import config

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, create_engine, ForeignKey

Base = declarative_base()

def get_connection():
    try:
        return psycopg2.connect(
            host = config('MYSQL_HOST'),
            user = config('MYSQL_USER'),
            password = config('MYSQL_PASSWORD'),
            database = config('MYSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex