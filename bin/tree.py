# -*- coding: utf-8 -*-

import os
import db
from generate import *
import json

def main():

	#JSON object for settings
	jsondata = open("conf.json")
	settings = json.load(jsondata)

	#datasource for database access
	datasource = db.db("ssvd.db")
	datasource.open()
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		#truncate database before new entries
		datasource.truncate(folder.lower())
		
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
						datasource.insert(folder.lower(), dirname.replace(fullpath,''), filename, int(os.stat(os.path.join(dirname, filename)).st_mtime))
						
	#Commit and close database when done
	datasource.close()
	
	#Generate webpages
	generate()
				
if __name__ == '__main__': main()
