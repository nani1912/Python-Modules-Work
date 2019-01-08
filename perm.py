#!usr/bin/python

import subprocess, os
#subprocess.call(['chmod', '777', '/root/python-work/os2.py'])

for root, dirs, files in os.walk('/root/python-work'):
    for d in dirs:
        os.chmod(os.path.join(root, d), 777)
    for f in files:
        os.chmod(os.path.join(root,f), 777)
