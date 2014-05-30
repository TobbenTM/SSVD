# -*- coding: utf-8 -*-

import sqlite3

class db:
	def __init__(self, dbname):
		self.dbname = dbname
		
	def setup(self, table):
		self.cursor.execute("CREATE TABLE %s (path text, file text, mod integer)" % table)
		
	def open(self):
		self.connection = sqlite3.connect(self.dbname)
		self.connection.text_factory = str
		self.cursor = self.connection.cursor()
		
	def insert(self, table, path, file, mod):
		self.cursor.execute("INSERT INTO %s VALUES (?, ?, ?)" % table, (path, file, mod))
		
	def getall(self, table):
		self.cursor.execute("SELECT * FROM %s" % table)
		return self.cursor.fetchall()
		
	def getrecent(self, table):
		self.cursor.execute("SELECT * FROM %s ORDER BY mod DESC LIMIT 10" % table)
		return self.cursor.fetchall()
		
	def truncate(self, table):
		self.cursor.execute("DELETE FROM %s" % table)
		
	def close(self):
		self.connection.commit()
		self.connection.close()