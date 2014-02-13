# -*- coding: utf-8 -*-

import os
#from db import *

def main():
	dir = "/mnt/DroboFS/Shares/MainShare/Serier"
	
	for dirname, subList, fileList in os.walk(dir):
		for filename in fileList:
			if ".AppleDouble" not in dirname:
				if ".mkv" in filename:
					print("%s, %s, %s" % (dirname, filename, os.stat(os.path.join(dirname, filename)).st_mtime))

				
if __name__ == '__main__': main()