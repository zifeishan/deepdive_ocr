#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys   # needed by most
import random   # random 
import yaml     # yaml parsing
import pprint   # pretty print

if __name__ == "__main__": 
  # ...
  labelpath = ''
  if len(sys.argv) == 2:
    path = sys.argv[1]
  elif len(sys.argv) == 3:
    path = sys.argv[1]
    labelpath = sys.argv[2]
  else:
    print 'Usage:',sys.argv[0],'<file> [labelfile]'
    sys.exit(1)

  lines = [l.rstrip('\n').split('\t') for l in open(path).readlines()]

  if labelpath != '': 
    labels = open(labelpath).readlines()
  else:
    labels = None

  print path
  fout = open(path+'.compare.txt', 'w')

  sub = 0
  for l in lines: 
    if len(l) < 5:
      print >>fout, ''
      continue

    if l[1] == l[2] or l[2] == '' or l[1] == '':
      print >>fout, '%2s %15s %15s  %3s %6s' % (l[0], l[1], l[2], l[3], l[4][:6]) + '\t'
    else:
      labelstr = ''
      if labels != None: 
        # label = labels[sub][1]
        parts = labels[sub].split(' ')
        if parts[1] != '': 
          print parts[0:2]

        if parts[0] == 'X1' or parts[0] == 'X2' or parts[0] == 'X3':
          label = parts[0][1]
          labelstr = '$'+label

          if label == '3' and len(l[1]) < 19 and parts[1] != '':
            # print '----',parts
            # if parts[1] != '':
            label = parts[1]
            print label

            labelstr = '$'+label

      print >>fout, '%2s %15s %15s  %3s %6s' % (l[0], l[1], l[2], l[3], l[4][:6]) + '\t|||' + labelstr
      
    sub += 1
  # print 'NonEmptyLines:',sub

  fout.close()
