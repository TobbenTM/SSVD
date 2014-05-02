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

	#file handlers
	index = open(settings["wwwpath"]+"/index.html", "w")

	#writing template, should be done in a slicker way really
	index.write("""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>SSVD</title>
	<link href="css/bootstrap.css" rel="stylesheet">
	<link href="css/ssvd.css" rel="stylesheet">
</head>
<body>
	<div class="site-wrapper">
		<div class="site-wrapper-inner container">
			<div class="masthead clearfix">
				<h3 class="masthead-brand">SSVD</h3>
			</div>
			<div class="row">
				<div class="col-md-6">
					<h1>Library:</h1>""")
	
	# Library
	
	index.write("<div class=\"panel-group\" id=\"MAIN\">");
	
	#looping through folders specified in settings
	for folder in settings["folders"]:
			
		all = datasource.getall(folder.lower())
		lastpath = ''
		
		index.write("""
<div class="panel panel-default">
	<div class="panel-heading">
		<h4 class="panel-title panel-head">
			<a data-toggle="collapse" data-parent="#MAIN" href="#{0}">
				{0}
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
					index.write("</div></div></div>")
						
				index.write("""
<div class="panel panel-default">
	<div class="panel-heading">
		<h4 class="panel-title">
			<a data-toggle="collapse" data-parent="#SEC" href="#{1}">
				{2}
			</a>
		</h4>
	</div>
	<div id="{1}" class="panel-collapse collapse">
		<div class="panel-body">
			<a href="video.html?video={0}{2}/{3}">{3}</a></br>
				""".format(folder, row[0].translate(None, ' !();,./-\'\\'), row[0], row[1]))
			else:
				index.write("""<a href="video.html?video={0}{1}/{2}">{2}</a></br>""".format(folder, row[0], row[1]))
			
			lastpath = row[0]
		
		index.write("</div></div></div></div></div></div>")
			
	index.write("""</div></div></div>
<div class="col-md-6 recent">
	<h1>Recently added:</h1>""")

	# Recent

	#looping through folders specified in settings
	for folder in settings["folders"]:
	
		recent = datasource.getrecent(folder.lower())
		
		index.write("<h3>{0}:</h3>".format(folder))
		
		#Generate recent list for current folder
		for row in recent:
			time = datetime.datetime.fromtimestamp(row[2]).strftime('%d/%m-%Y  %H:%M')
			index.write("<p>{3} - <a href=\"/video.html?video={0}{1}/{2}\">{2}</a></p>".format(folder, row[0], row[1], time))
			index.write("<p style=\"font-size:12px\">({0})</p>".format(row[0]))

	index.write("""</div></div></div></div>
<script src="js/jquery.js"></script>
<script src="js/bootstrap.js"></script>
</body>
</html>""")
	
	#Close and commit database connection
	datasource.close()

	#Close file IO
	index.close()