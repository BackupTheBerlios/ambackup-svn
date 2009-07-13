# ambackup.py - v0.01 2009-07-05 11:25AM
# Modular backup script for abyle
#
# CHANGELOG:
# 	- 2009-07-05 {hps}: input.filesystem module
#
# TODO:
# 	- implement more modules for input (psql, mysql), output (tar, ftp) and extensions (syslog)
#		output modules should do all the backup management, delete old backups, move them around for monthly backups etc.
#		(or maybe as an extension?)
#
# BUGS:
# 
# Module syntax (draft):
# input:
# 	modulename.backup(source, destination, [module_options])
# 	source=directories, databases,...
# 	destination=global_backup_directory + todays date, every module should use dst_date and create a own directory dst_date/modulename
#		for example: dst_date/filesystem
#	[module_options]=database logins, special copy options,...
#
# output:
#	...
#

from ambackuplib.input import filesystem
from datetime import date,timedelta
import os

debug=1 # set to 1 to enable debugging statements

# global backup directory
dst="/home/hps/backup"

# activate modules
module_filesystem=1

# source
filesystem_src=["/home/hps/test","/home/hps/kdesvn-build-1.9.1","/home/hps/mathematica patch"]

# ---

d = date.today()+timedelta(1)
dst_date=os.path.join(dst, d.strftime("%y_%m_%d"))

if debug:
	while os.path.exists(dst_date):
		d = d + timedelta(1)
		dst_date=os.path.join(dst, d.strftime("%y_%m_%d"))

if module_filesystem:
	filesystem.backup(filesystem_src, dst_date)
	
