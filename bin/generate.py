# -*- coding: utf-8 -*-

import db
import json
import time
import datetime

def generate():

	#JSON object for settings
	jsondata = open("conf.json")
	settings = json.load(jsondata)
	
	#datasource for database access
	datasource = db.db("ssvd.db")
	datasource.open()
	
	recent = datasource.getrecent("serier")
	
	for row in recent:
		time = datetime.datetime.fromtimestamp(row[2]).strftime('%d/%m-%Y  %H:%M')
		print("<p>{3} - <a href=\"/video.html?video={0}{1}/{2}\">{2}</a></p>".format("Serier", row[0], row[1], time))
		print("<p>({0})</p>".format(row[1]))
		
	datasource.close()