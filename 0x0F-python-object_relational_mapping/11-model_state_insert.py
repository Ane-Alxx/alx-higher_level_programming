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
		new_state = State(name="Louisiana")
		db_session.add(new_state)
		db_session.commit()
		print(new_state.id)
		db_session.close()
