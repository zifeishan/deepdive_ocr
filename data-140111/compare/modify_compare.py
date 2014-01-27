#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys   # needed by most
import random   # random 
import yaml     # yaml parsing
import pprint   # pretty print

if __name__ == "__main__": 
  # ...
  if len(sys.argv) == 2:
    path = sys.argv[1]
  else:
    print 'Usage:',sys.argv[0],'<file>'
    sys.exit(1)

  lines = [l.rstrip('\n') for l in open(path).readlines()]

  print path
  fout = open(path+'.mod', 'w')

  for l in lines: 
    if len(l) == 0: # empty line
      print >>fout, l
      continue

    if '|||' in l or '///' in l:  # already tagged
      print >>fout, l
    else:
      w1 = l[3:18].strip(' ') 
      w2 = l[19:19+15].strip(' ')
      if w1 != w2:
        l = l + '///'
      print >>fout, l
            
  fout.close()
