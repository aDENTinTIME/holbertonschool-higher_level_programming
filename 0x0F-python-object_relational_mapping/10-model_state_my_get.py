#!/usr/bin/python3


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """Prints corisponding State object (id) to passed name."""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]
    flag = True

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        if searched == state.name:
            print(state.id)
            flag = False

    if flag:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
