#!/usr/bin/python3


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """Adds the State object 'Louisiana' to a database"""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    new_state = "Louisiana"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    add_me = State(name=new_state)

    session.add(add_me)
    session.commit()

    print(add_me.id)

    session.close()


if __name__ == "__main__":
    main()
