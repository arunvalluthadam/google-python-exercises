#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dire):
    lis = []
    filenames = os.listdir(dire)
    for i in filenames:
        part = r'\w+__\w+__.\w+'
        r = re.search(part,i)
        if r:
            a = r.group()
            lis.append("\'"+os.path.abspath(a+"\'"))
    print lis
#    for i in lis:
        

#get_special_paths('/home/simplans/local-project/google-python-exercises/copyspecial')

def copy_to(paths,dire):
    filenames = os.listdir(paths)
    for i in filenames:
        part = r'\w+__\w+__.\w+'
        r = re.search(part,i)
        if r:
            a = r.group()
            abspath = os.path.abspath(a)
            if os.path.exists(dire):
                shutil.copy(abspath,dire)
            else:
                os.mkdir(dire)
                shutil.copy(abspath,dire)

#copy_to('/home/simplans/local-project/google-python-exercises/copyspecial','/home/simplans/local-project')

def zip_to(paths,zippath):
    cmd = 'zip -j temp.zip -b '+zippath
    filenames = os.listdir(paths)
    for i in filenames:
        part = r'\w+__\w+__.\w+'
        r = re.search(part,i)
        if r:
            a = r.group()
            abspath = os.path.abspath(a)
            if os.path.exists(zippath):
                commands.getoutput(cmd+' '+abspath)
            else:
                os.mkdir(zippath)
                commands.getoutput(cmd+' '+abspath)


zip_to('/home/simplans/arunvalluthadam/google-python-exercises/copyspecial','/home/simplans/arunvalluthadam/google-exercises')

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
