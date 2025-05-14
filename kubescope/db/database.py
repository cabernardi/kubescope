from typing import List

import sqlalchemy
from sqlalchemy import select
from sqlmodel import Field, Session, SQLModel, create_engine

from kubescope.config import (
    DB_DRIVER_NAME,
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USERNAME,
)
from kubescope.exceptions import DatabaseNotConfigured


class Person(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True)


def check_engine():
    if not engine:
        raise DatabaseNotConfigured("Database engine is not initialized. Check your database connection settings.")


def create_db():
    check_engine()
    SQLModel.metadata.create_all(engine)


def drop_db():
    check_engine()
    SQLModel.metadata.drop_all(engine)


def get_people() -> List[Person]:
    check_engine()

    query = select(Person)
    with Session(engine) as session:
        result = session.exec(query)
        people = result.scalars().all()
    return people


def add_person(name: str) -> Person:
    check_engine()
    person = Person(name=name)
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
    return person


try:
    connection_url = sqlalchemy.engine.URL.create(
        drivername=DB_DRIVER_NAME,
        username=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
        port=DB_PORT,
    )

    engine = create_engine(connection_url)
    create_db()
except Exception as e:
    print(f"Database connection error: {e}")
    engine = None
