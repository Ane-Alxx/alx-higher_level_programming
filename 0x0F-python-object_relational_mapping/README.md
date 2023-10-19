**Introduction**
-----------------------------------------------------

This project is a tutorial on how to use databases and Python together.

**MySQLdb and SQLAlchemy**
-----------------------------------------------------

MySQLdb is a module that allows you to connect to a MySQL database and execute SQL queries. SQLAlchemy is an ORM (Object Relational Mapper) that allows you to interact with your database using Python objects.

**Benefits of using an ORM**
------------------------------------------------------------

There are several benefits to using an ORM, including:

* **Abstraction:** An ORM abstracts away the underlying database details, so you don't need to know SQL to interact with your database.
* **Productivity:** An ORM can help you to write your code more quickly and efficiently.
* **Portability:** An ORM can make your code more portable, as it can be used to connect to different types of databases.

**Example**
----------------------------------------------------------------

The following code shows how to use SQLAlchemy to query for all states in a MySQL database:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('mysql+mysqldb://root:root@localhost/my_db')
session = Session(engine)

State = session.query(State).all()

for state in State:
    print(state.name)
```

This code will print out the names of all states in the database.

**Conclusion**
----------------------------------------------------

SQLAlchemy is a powerful and popular ORM that can help you to write more efficient and portable Python code. For more information, please refer to the resources listed below.

**Resources**
--------------------------------------------------------------------

* SQLAlchemy tutorial
* SQLAlchemy documentation

In addition to the benefits listed above, ORMs can also help to improve the quality of your code by:

* Reducing the amount of boilerplate code that you need to write.
* Enforcing data integrity constraints.
* Making it easier to test your code.

If you are developing a Python application that needs to interact with a database, I highly recommend using an ORM like SQLAlchemy.

Tasks
---------------------------------------------------------------------
	- 0-select_states.py 
	- 1-filter_states.py
	- 2-my_filter_states.py
	- 3-my_safe_filter_states.py
	- 4-cities_by_state.py
	- 5-filter_cities.py
	- model_state.py
	- 7-model_state_fetch_all.py
	- 8-model_state_fetch_first.py
	- 9-model_state_filter_a.py
	- 10-model_state_my_get.py
	- 11-model_state_insert.py
	- 12-model_state_update_id_2.py
	- 13-model_state_delete_a.py
	- model_city.py, 14-model_city_fetch_by_state.py
	- ... and the advanced questions
