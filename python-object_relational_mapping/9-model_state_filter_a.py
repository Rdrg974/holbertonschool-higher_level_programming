#!/usr/bin/python3
"""
This script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))

    session.close()
