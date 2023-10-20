#!/usr/bin/python3
"""
Lists all states from a database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
		db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
													 passwd=argv[2], db=argv[3], charset="utf8")
		cur = db_conn.cursor()
		cur.execute("SELECT * FROM states ORDER BY states.id ASC")
		db_rows = cur.fetchall()
		for row in db_rows:
				if row[1].startswith("N"):
						print(row)
		cur.close()
		db_conn.close()
