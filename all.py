#!usr/bin/python


import os, subprocess, random

subprocess.call('vmstat')
#subprocess.call('lsof')
#subprocess.call('netstat')

cmd = 'netstat -antp'
print os.system(cmd)

swap = 'free -m'        
print os.system(swap)

port = 'lsof -i'
print os.system(port)

disk = 'fdisk -l'
print os.system(disk)

#for disk in os.walk('/root/python-work/Python'):
#    diskusage = 'du -h'
#subprocess.call(diskusage, 'shell=True')
#    print os.system(diskusage)






