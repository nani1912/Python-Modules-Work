#!/usr/bin/env python
import psutil
# gives a single float value
print "cpu usage is :",  (psutil.cpu_percent())
# gives an object with many fields
print "Memory usage is :", (psutil.virtual_memory())
# you can convert that object to a dictionary 
#print (dict(psutil.virtual_memory()._asdict()))

print "cpu_count is :" , (psutil.cpu_count())




#import psutil
#print(psutil.cpu_percent())
#print(psutil.virtual_memory()) #  physical memory usage
