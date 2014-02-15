# -*- coding: utf-8 -*-

import db
import json

def main():

	# TODO: Copy required files to wwwpath

	#JSON object for settings
	jsondata = open("conf.json")
	settings = json.load(jsondata)

	#datasource for database access
	datasource = db.db("ssvd.db")
	datasource.open()
	
	print("Starting database install...")
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		#Creating tables for each of the folders in settings
		datasource.setup(str(folder.lower()))	
		print("Created table: "+str(folder.lower()))

	print("Database setup completed")
	
	#Commit and close database when done
	datasource.close()

if __name__ == '__main__': main()