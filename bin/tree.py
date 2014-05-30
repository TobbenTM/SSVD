# -*- coding: utf-8 -*-

import os
import db
from generate import *
import json

def main():

	#JSON object for settings
	jsondata = open(os.path.dirname(os.path.abspath(__file__)) + "/conf.json")
	settings = json.load(jsondata)

	#datasource for database access
	datasource = db.db(os.path.dirname(os.path.abspath(__file__)) + "/ssvd.db")
	datasource.open()
	
	print("Starting crawl..")
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		if(folder == ""):
			tablename = "Videos"
		else:
			tablename = folder.lower()
	
		print("Crawling " + folder)
	
		#truncate database before new entries
		datasource.truncate(tablename)
		
		fullpath = str(settings["fullpath"]) + str(folder)
		for dirname, subList, fileList in os.walk(fullpath):
		
			#Sort lists alphabetically and case insensitive
			subList.sort(key = lambda s: s.lower())
			fileList.sort(key = lambda s: s.lower())
			
			for filename in fileList:
			
				#Ignores all AppleDouble directories
				if ".AppleDouble" not in dirname:
				
					#Checks if filename contains any wanted extensions
					if any(str(ext) in filename for ext in settings["filetypes"]):

						#Insert into database
						datasource.insert(tablename, dirname.replace(fullpath,''), filename, int(os.stat(os.path.join(dirname, filename)).st_mtime))
						
	print("Done crawling")
						
	#Commit and close database when done
	datasource.close()
	
	#Generate webpages
	generate()
				
if __name__ == '__main__': main()
