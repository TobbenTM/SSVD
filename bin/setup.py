# -*- coding: utf-8 -*-

import db
import json
from distutils import dir_util

def main():

	# TODO: Setup cron

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


	print("Copying files to web server...")

	#copying necessary files to wwwpath
	log = dir_util.copy_tree("../www/", settings["wwwpath"])
	smbpath = open(settings["wwwpath"]+"/js/smbpath.js", "w")
	smbpath.write("var smbpath = \""+settings["sambapath"]+"\";")
	smbpath.close()

	print("Completed copying files")


	#Commit and close database when done
	datasource.close()

if __name__ == '__main__': main()