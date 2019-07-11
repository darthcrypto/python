#!/bin/env/python

#python 2.7

from subprocess import check_output

def hostname_status():
   value = check_output("hostname")
   print(value)

if __name__ == "__main__":
  hostname_status()
