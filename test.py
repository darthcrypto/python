#!/bin/env/python


###2.7


SUCCESS
###print both return code and error message
#from subprocess import Popen, PIPE

#p = Popen(["cat", "/tmp/alligator"], stdout=PIPE)
#output = p.communicate()[0]
#print(p.returncode)

---------------



###print just the error message":
#import subprocess
#import os
#result = subprocess.Popen(["cat", "/tmp/alligator"], stdout=fp)
#text = result.communicate()[0]
#returncode = result.returncode
#print(returncode)




import subprocess
import os
with open(os.devnull, 'w') as fp:
    cmd = subprocess.Popen(["cat", "/tmp/alligator"], stdout=fp)
    text = result.communicate()[0]
    returncode = result.returncode
    print(returncode)
~
