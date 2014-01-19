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

  lines = [l.rstrip('\n').split('\t') for l in open(path).readlines()]

  print path
  fout = open(path+'.compare.txt', 'w')

  for l in lines: 
    if len(l) < 5:
      print >>fout, ''
      continue
    if l[1] == l[2] or l[2] == '' or l[1] == '':
      print >>fout, '%2s %15s %15s  %3s %6s' % (l[0], l[1], l[2], l[3], l[4][:6]) + '\t'
    else:
      print >>fout, '%2s %15s %15s  %3s %6s' % (l[0], l[1], l[2], l[3], l[4][:6]) + '\t|||'
      
    
  fout.close()
