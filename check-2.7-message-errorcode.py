#!/bin/env/python

###2.7
###print both return code and error message

from subprocess import Popen, PIPE

p = Popen(["cat", "/tmp/alligator"], stdout=PIPE)
output = p.communicate()[0]
print(p.returncode)
