#!/usr/bin/python3


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """Lists first State object in a database."""
    """
    Considered using this.

    :param close_with_result: Passed to :meth:`.Engine.connect`,
      indicating the :class:`.Connection` should be considered
      "single use", automatically closing when the first result set is
      closed.  This flag only has an effect if this :class:`.Session` is
      configured with ``autocommit=True`` and does not already have a
      transaction in progress.
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main()
