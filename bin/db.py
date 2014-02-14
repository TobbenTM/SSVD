# -*- coding: utf-8 -*-

import sqlite3

class db:
	def __init__(self, dbname):
		self.dbname = dbname
		
	def setup(self, tables):
		for s in tables:
			self.cursor.execute("CREATE TABLE {0} (path text, file text, mod integer)".format(s))
		
	def open(self):
		self.connection = sqlite3.connect(self.dbname)
		self.connection.text_factory = str
		self.cursor = self.connection.cursor()
		
	def insert(self, table, path, file, mod):
		query = "INSERT INTO {0} VALUES ('{1}','{2}','{3}')".format(table, path, file, mod)
		print(query)
		self.cursor.execute("INSERT INTO serier VALUES (?, ?, ?)", (path, file, mod))
		
	def getall(self, table):
		self.cursor.execute("SELECT * FROM {0}".format(table))
		return self.cursor.fetchall()
		
	def close(self):
		self.connection.commit()
		self.connection.close()