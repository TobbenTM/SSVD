# -*- coding: utf-8 -*-

import os
import db

def main():
	datasource = db.db("ssvd.db")
	datasource.open()
	#datasource.setup(["serier"])

	dir = "/mnt/DroboFS/Shares/MainShare/Serier"
	suffix = (".mkv", ".avi", ".mp4")
	i = 0;
	
	for dirname, subList, fileList in os.walk(dir):
	
		#Sort lists alphabetically and case insensitive
		subList.sort(key = lambda s: s.lower())
		fileList.sort(key = lambda s: s.lower())
		
		for filename in fileList:
		
			#Ignores all AppleDouble directories
			if ".AppleDouble" not in dirname:
			
				#Checks if filename contains any wanted extensions
				if any(ext in filename for ext in suffix):
					
					i += 1
					#print("%s; %s, %s, %s" % ("Items: " + str(i), dirname.replace(dir, ''), filename, int(os.stat(os.path.join(dirname, filename)).st_mtime)))
					#print("<a href=\"/video.html?video=/Serier{0}/{1}\">{1}</a>".format(dirname.replace(dir, ''), filename))
					datasource.insert("serier", dirname.replace(dir,''), filename, int(os.stat(os.path.join(dirname, filename)).st_mtime))
					
	datasource.close()
				
if __name__ == '__main__': main()
