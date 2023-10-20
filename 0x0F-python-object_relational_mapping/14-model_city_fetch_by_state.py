#!/usr/bin/python3
"""
Lists states from a database.
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
		engine = create_engine(
				'mysql+mysqldb://{}:{}@localhost:3306/{}'
				.format(argv[1], argv[2],
								argv[3]), pool_pre_ping=True)
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		db_session = Session()
		results = db_session.query(City, State).\
				filter(City.state_id == State.id).all()
		for city, state in results:
				print("{}: ({}) {}".format(state.name, city.id, city.name))
		db_session.commit()
		db_session.close()
