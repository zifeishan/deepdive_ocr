#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

if __name__ == "__main__": 
  if len(sys.argv) == 2:
    path = sys.argv[1]
  else:
    print 'Usage:',sys.argv[0],'<file>'
    sys.exit(1)

  lines = [l.strip(' \n').split(' |||') for l in open(path).readlines()]

  # # Neglect sentences that all right
  # sentences = open(path).read().split('\n\n')
  # sentences_filtered = [s.split('\n') for s in sentences if '|||' in s]
  

  lines = [l.strip(' \n').split(' |||') for l in open(path).readlines()]

  tags = [l.strip() for l in open('rule-tags.md').readlines()]
  fout = open('knowledge-stat.md', 'w')

  know_map = {t:0 for t in tags}
  totnum = 0
  solvenum = 0
  for l in lines: 
    if len(l) < 2 or l[1] == "":
      continue

    num = int(l[0])
    totnum += num
    if '?' in l[1]:
      continue
    else:
      solvenum += num
    l[1] = l[1].replace('?', '')  
    l[1] = re.sub('\(.*\)','',l[1])
    know_used = l[1].split(',')
    for k in know_used:
      if k == '':
        continue
      if k not in know_map:
        # know_map[k] = 0
        continue
      know_map[k] += num

  print >>fout, 'Total:', totnum
  print >>fout, 'Solved:', solvenum, '%.4f' % (solvenum/float(totnum))

  # for k in sorted(know_map, key=know_map.get, reverse=True):
  #   print >>fout, '%10s\t%3d\t%.4f' % (k, know_map[k], float(know_map[k]) / totnum)

  for t in tags:
    print >>fout, '%10s\t%3d\t%.4f' % (t, know_map[t], float(know_map[t]) / totnum)

  fout.close()

  tax = open('./taxonomy-nonumber.md').read()
  patterns = re.findall('\[.*\]', tax)
  print 'Find patterns:',patterns
  repl_map = {}
  for p in patterns:
    tag = p.strip('[]')
    if tag not in know_map: continue
    val = '['+tag+'\t'+ '%.2f%%' % (know_map[tag] * 100.0 / totnum) + ']'
    pat = '\\['+tag+'\\]'
    repl_map[pat] = val
    print 'Replace',pat,'with',val

  for p in repl_map:
    tax = re.sub(p, repl_map[p], tax)
    print 'Replaced',p,'with',repl_map[p]
    print 'Current tax:',tax[:300]

  fout = open('taxonomy-numbered.md', 'w')
  print >>fout, tax
  fout.close()


  from numpy import *
  import matplotlib.pyplot as plt
  from pylab import *

  # exp = [0.5255,  0.3284,  0.4040, 0.6870,  0.6126,  0.6469,0.8517,  0.6376,  0.7271]
  exp = [know_map[tag] * 100.0 / totnum for tag in sorted(know_map, key=know_map.get, reverse=True)]
  err = [0.02] * len(know_map)

  width = 0.2       # the width of the bars: can also be len(x) sequence
  left = [ i * width for i in range(0,len(know_map))]
  tagnames = [ tag for tag in know_map]

  matplotlib.rcParams.update({'font.size': 12})

  # plt.xticks(left, [n for n in know_map] )
  for i in range(0,len(know_map)):
    plt.text(left[i], exp[i], tagnames[i])


  fig = plt.figure()
  ax = fig.add_subplot(111)
  rects = ax.bar(left = left, height = exp, width = width, 
    bottom = None, yerr = err
    # ,
    # ecolor = 'black',
    # color=colors
    )

  grid(True)
  xlabel('Knowledge')
  ind = np.arange(len(know_map))    # the x locations for the groups
  
  

  ylabel('Used in (%)')

  # plt.legend(['P', 'R', 'F1'], 'upper left')

  plt.savefig('knowledge-errorbar.eps')
  # plt.show()
