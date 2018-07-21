#!/usr/bin/python3


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """Lists all State objects that contain the letter 'a' in a database."""

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
