#!/bin/env/python

#python 2.7
###check output of command

from subprocess import check_output

def hostname_status():
   command = ["cat", "/tmp/alligator"]
   value = check_output(command)
   print(value)

if __name__ == "__main__":
  hostname_status()
