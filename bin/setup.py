# -*- coding: utf-8 -*-

import os
import db
import json
import os
from distutils import dir_util

def main():

	# TODO: Setup cron

	#JSON object for settings
	jsondata = open(os.path.dirname(os.path.abspath(__file__)) + "/conf.json")
	settings = json.load(jsondata)

	#datasource for database access
	datasource = db.db(os.path.dirname(os.path.abspath(__file__)) + "/ssvd.db")
	datasource.open()
	
	print("Starting database install...")
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		if(folder == ""):
			tablename = "Videos"
		else:
			tablename = str(folder.lower())
	
		#Creating tables for each of the folders in settings
		datasource.setup(tablename)	
		print("Created table: " + tablename)

	print("Database setup completed")

	print("Copying files to web server...")

	#copying necessary files to wwwpath
	log = dir_util.copy_tree(os.path.dirname(os.path.abspath(__file__)) + "/../www/", settings["wwwpath"])
	smbpath = open(settings["wwwpath"]+"/js/smbpath.js", "w")
	smbpath.write("var smbpath = \""+settings["sambapath"]+"\";")
	smbpath.close()

	print("Completed copying files")

	#Commit and close database when done
	datasource.close()
	
if __name__ == '__main__': main()
