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
	
	totalfiles = 0
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		recent = datasource.getrecent(folder.lower())
		
		print("<h3>{0}:</h3>".format(folder))
		
		#Generate recent list for current folder
		for row in recent:
			time = datetime.datetime.fromtimestamp(row[2]).strftime('%d/%m-%Y  %H:%M')
			print("<p>{3} - <a href=\"/video.html?video={0}{1}/{2}\">{2}</a></p>".format(folder, row[0], row[1], time))
			print("<p>({0})</p>".format(row[0]))
	
	
	print("<div class=\"panel-group\" id=\"MAIN\">");
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
			
		all = datasource.getall(folder.lower())
		lastpath = ''
		totalfiles += len(all)
		
		print("""
<div class="panel panel-default">
	<div class="panel-heading">
		<h4 class="panel-title panel-head">
			<a data-toggle="collapse" data-parent="#MAIN" href="#{0}">
				<span class="glyphicon glyphicon-hdd"></span>  {0}
			</a>
		</h4>
	</div>	
	<div id="{0}" class="panel-collapse collapse">
		<div class="panel-body">
			<div class="panel-group" id="SEC">
		""".format(folder))
		
		#Generate library for current folder
		for row in all:
			if row[0] not in lastpath:
				if lastpath is not '':
					print("</div></div></div>")
						
				print("""
<div class="panel panel-default">
	<div class="panel-heading">
		<h4 class="panel-title">
			<a data-toggle="collapse" data-parent="#SEC" href="#{1}">
				<span class="glyphicon glyphicon-folder-open"></span>  {2}
			</a>
		</h4>
	</div>
	<div id="{1}" class="panel-collapse collapse">
		<div class="panel-body">
			<a href="/video.html?video={0}{2}/{3}"><span class="glyphicon glyphicon-play-circle"></span>  {3}</a></br>
				""".format(folder, row[0].translate(None, ' !();,./-\''), row[0], row[1]))
			else:
				print("""<a href="/video.html?video={0}{1}/{2}"><span class="glyphicon glyphicon-play-circle"></span>  {2}</a></br>""".format(folder, row[0], row[1]))
			
			lastpath = row[0]
		
		print("</div></div></div></div></div></div>")
			
	print("</div></div></div><p>A total of {0} files indexed.</p>".format(totalfiles))
	
	datasource.close()
	
	
	
	