#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  lis1 = []
  lis2 = []
  for i in open(filename):
    part1 = r'/edu/languages/google-python-class/images/puzzle/.......jpg'
    part2 = r'/edu/languages/google-python-class/images/puzzle/............jpg'
    r = re.search(part1,i)
    if r:
        a = r.group()
        lis1.append(a)
    else:
        e = re.search(part2,i)
        if e:
            b = e.group()
            lis1.append(b)
  sort = sorted(set(lis1))
  for i in sort:
      a = r'http://code.google.com'
      b = a + i
#      f = open('sorted_url.google.com','a')    
#      f.write(b+"\n")
#      f.close()

      print b

#read_urls('place_code.google.com')

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  f = open('index.html','w')
  f.write('<html>\n<body>\n')
  imgval = 0
  for url in open(img_urls):
#      strurl = url.strip()
      chg = '/img%d.jpg' % imgval
      print "Downloading .... ", url
#      urllib.urlretrieve(url,dest_dir+chg)
      f.write('<img src='+dest_dir+"/img%d.jpg"'>' % imgval)
      imgval += 1
  f.write('\n</body>\n</html>')
  f.close()

download_images('sorted_url.google.com', '/home/simplans/local-project/google-python-exercises/logpuzzle/images')

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
