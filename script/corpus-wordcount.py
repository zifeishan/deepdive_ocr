import os, sys, re, operator

# Clean the word to only \W
def Strip(word):
  # return word.strip('.,?!;:')
  return re.sub('\W', '', word)
  # print string

wordcount = {}

base = '../data/'
for f in os.listdir('../data/'):
  if f.endswith('.output.txt'):
    print 'Process,', f
    words = [line.strip().split('\t') for line in open(base + f).readlines()]
    for w in words:
      if len(w) <= 1: continue
      # if w[1] != w[2]: continue
      for opt in [w[1], w[2]]:
        opt = Strip(opt)
        if len(opt) == 0: continue
        if opt not in wordcount:
          wordcount[opt] = 0
        wordcount[opt] += 1

fout = open('corpus-wordcount.txt', 'w')
for pair in sorted(wordcount.iteritems(), key=operator.itemgetter(1), reverse=True):
  print >>fout, pair[0]+'\t'+str(pair[1])

fout.close()


