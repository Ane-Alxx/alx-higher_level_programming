#!/usr/bin/python3
"""
Lists states from a database.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
		engine = create_engine(
				'mysql+mysqldb://{}:{}@localhost/{}'
				.format(argv[1], argv[2],
								argv[3]), pool_pre_ping=True)
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		db_session = Session()
		for state in db_session.query(State).\
						filter(State.name.like('%a%')).order_by(State.id).all():
				print("{}: {}".format(state.id, state.name))
		db_session.close()
