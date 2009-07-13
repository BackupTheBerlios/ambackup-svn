# ambackuplib module: import.filesystem - v0.01 2009-07-05 11:25AM
#
# CHANGELOG:
# 	- 2009-07-05 {hps}: first copy function
#
# TODO:
# 	- implement more modules for input (psql, mysql) and output (tar)
#
# BUGS:
# 

from shutil import *
import os

def backup(src, dst, symlinks=False, ignore=None):
	dst_filesystem=os.path.join(dst, "filesystem")
	if os.path.exists(dst_filesystem):
		print "Backup directory \""+ dst_filesystem + "\" already exists!"
	else:
		for dir in src:
			print "Creating backup: \"" + dir
			copytree(dir, os.path.join(dst_filesystem, os.path.basename(dir)), symlinks, None)

