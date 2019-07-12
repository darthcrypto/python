#!/bin/env/python

#check for python version 2, only returns error code

import subprocess
import os

def check():
  commandA = "cat /tmp/alligator"
  FNULL = open(os.devnull, 'w')
  exit_code = subprocess.call(commandA.split(), stdout=FNULL, stderr=subprocess.STDOUT)
  print(exit_code)

if __name__ == "__main__":
  check()
