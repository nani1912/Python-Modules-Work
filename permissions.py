#!usr/bin/python

import subprocess, os
subprocess.call(['chmod','755','/root/randompwd.py', '/root/os1.py','/root/os2.py','/root/permissions.py'])

print "Below files are current working directory files: \n %s" %os.listdir(os.getcwd())



