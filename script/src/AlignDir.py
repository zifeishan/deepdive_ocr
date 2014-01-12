import sys, os
from preprocess import *
from pyquery import PyQuery
import re

def AlignDir(base, output_base, inputs):

  for filename in inputs:
    filename = filename.rstrip('\n')
    path = base + filename + '/'
    if not os.path.exists(path):
      print path, 'does not exist.'
      continue

    outputbase = output_base + filename
    Align.AlignFromPath(path, outputbase)

    # if float(filename) < 17825:  # continue on last time
    #   continue
    
if __name__ == "__main__": 
  if len(sys.argv) == 2:
    base = sys.argv[1]
  else:
    print 'Usage:', sys.argv[0],'<dirbase>'
    base = '../../input/'
    print 'Use default URL:', base

  inputs = open('input_list.txt').readlines()

  AlignDir(base, '../../data-140111/', inputs)
