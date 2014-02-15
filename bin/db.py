# -*- coding: utf-8 -*-

import sqlite3

class db:
	def __init__(self, dbname):
		self.dbname = dbname
		
	def setup(self, table):
		self.cursor.execute("CREATE TABLE {0} (path text, file text, mod integer)".format(table))
		
	def open(self):
		self.connection = sqlite3.connect(self.dbname)
		self.connection.text_factory = str
		self.cursor = self.connection.cursor()
		
	def insert(self, table, path, file, mod):
		self.cursor.execute("INSERT INTO " + table + " VALUES (?, ?, ?)", (path, file, mod))
		
	def getall(self, table):
		self.cursor.execute("SELECT * FROM {0}".format(table))
		return self.cursor.fetchall()
		
	def getrecent(self, table):
		self.cursor.execute("SELECT * FROM {0} ORDER BY mod DESC LIMIT 15".format(table))
		return self.cursor.fetchall()
		
	def truncate(self, table):
		self.cursor.execute("DELETE FROM {0}".format(table))
		
	def close(self):
		self.connection.commit()
		self.connection.close()