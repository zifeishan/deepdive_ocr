import os, sys, re, operator

# TIMEOUT tool
from functools import wraps
from pyquery import PyQuery  # support url parsing
import errno
import os
import signal

class TimeoutError(Exception):
  pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
  def decorator(func):
    def _handle_timeout(signum, frame):
      raise TimeoutError(error_message)

    def wrapper(*args, **kwargs):
      signal.signal(signal.SIGALRM, _handle_timeout)
      signal.alarm(seconds)
      try:
        result = func(*args, **kwargs)
      finally:
        signal.alarm(0)
      return result

    return wraps(func)(wrapper)

  return decorator

@timeout(5)
def PyQueryTimeOut(url):
  # print '-- Fetching:', url
  return PyQuery(url = url)

def PyQueryTimeOutRetry(url, retry = 3):
  retries = 0
  pq = None
  while retries < retry:
    try:
      pq = PyQueryTimeOut(url)
      break
    except TimeoutError, HTTPError:
      retries += 1
  if pq == None: 
    raise TimeoutError
  return pq


import enchant
dictionary = enchant.Dict("en_US")
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import os,sys   # needed by most
import urllib
from pyquery import PyQuery  # support url parsing
import re
# from util import *
import pickle, json
import shutil

g_dict = {}
g_path = 'web_occur_dict.json'
g_path_backup = 'web_occur_dict-backup.json'
g_counter = 0


def ReadDict(path = g_path):
  global g_dict
  try:
    fin = open(path, 'r')
  except IOError:
    return
  g_dict = json.load(fin)  # global dict
  print 'Loaded Dictionary of size:', len(g_dict)

def WriteDict(path = g_path):
  global g_dict
  print 'Copying Dictionary file:'
  try:
    shutil.copyfile(path, g_path_backup)
  except IOError:
    x = 1
  fout = open(path, 'w')
  json.dump(g_dict, fout, indent=1)
  fout.close()
  print 'Dictionary saved to:', path

def Transform(word):
  ori = word
  word = Strip(word)
  word = word.replace(' ', '+')
  word = re.sub(r"[^a-zA-Z0-9\-+\.]", "", word)
  # print ori, word
  return word

def Occur(word):
  global g_dict

  word = Transform(word)

  if word in g_dict:
    # print 'Found!', word, g_dict[word]
    return math.log(g_dict[word] + 1)

  # url = 'http://www.google.com/search?q='+word
  url = 'http://www.bing.com/search?q=%2b'+word
  # +'&filters=rcrse%3a"1"&FORM=RCRE'
  # print url
  
  try:
    pq = PyQueryTimeOutRetry(url = url, retry = 3)
  except TimeoutError:
    print 'Timeout!', word
    return 0

  counts = pq.find('.sb_count')
  if counts == None or counts.text() == None:
    count = 0
    g_dict[word] = count
    return math.log(count + 1)

  try:
    count = int(counts.text().rstrip(' results').replace(',', ''))
  except Error:
    print 'Error:', x.text()
    count = 0
  
  global g_counter
  g_counter += 1

  if g_counter % 30 == 0:
    WriteDict(g_path)

  g_dict[word] = count
  return math.log(count + 1)

def DictValid(word):
  # word = word.strip('.,?!;')
  word = Strip(word)
  if len(word) == 0:
    return 0
  if dictionary.check(word): # word exists
    return 1
  else:
    return 0


# Clean the word to only \W
def Strip(word):
  # return word.strip('.,?!;:')
  return re.sub('[^a-zA-Z\-]', '', word)
  # print string

# wordcount = {}

fout = open('bothwrong-tolabel-noweb-10255+.txt', 'w')

corpuspath = 'corpus-wordcount.txt'
corpus = {
  l.strip().split('\t')[0]:
  l.strip().split('\t')[1] 
  for l in open(corpuspath).readlines()
}


existing = set()
base = '../data/'
for f in os.listdir('../data/'):
  # searchfiles = ['158', '156']
  # searchfiles = ['17360', '10903', '12966', '19007', '13156.1', '10618', '19668.1']
  # searchfiles = ['19008','19009','19676','1330','18860','19045']
  searchfiles = ['10255','18557','14150','15460','19227','13908','10137','19007','17825','18050','10504','10432','12117','17756','19240','13588','13909','14309','13035','16596','13326','13268','19276','19020','16979','13031','19589']
  if f.endswith('.output.txt'):
    if f.rstrip('output.txt') not in searchfiles:
      continue
    print 'Process,', f
    words = [line.strip().split('\t') for line in open(base + f).readlines()]
    for w in words:
      if len(w) < 9: continue
      # if w[1] != w[2]: continue
      options = [Strip(w[2]), Strip(w[1])]
      if options[0] == options[1]: continue
      if options[0] in existing or options[1] in existing:
        continue

      if len(options[1]) < 4 or len(options[0]) < 4: 
        continue
      if options[0] in corpus and corpus[options[0]] > 3:
        continue
      if options[1] in corpus and corpus[options[1]] > 3:
        continue
      if not DictValid(options[1]) and not DictValid(options[0]) and Occur(options[1]) < 5 and Occur(options[0]) < 5:
        print '\t'.join(options),'\t',w[9],'\t',f.rstrip('.output.txt')
        print >>fout, '|','\t'.join(options),'\t',w[9],'\t',f.rstrip('.output.txt')
        fout.flush()
        existing.add(options[0])
        existing.add(options[1])
        # raw_input()

# fout = open('corpus-wordcount.txt', 'w')
# for pair in sorted(wordcount.iteritems(), key=operator.itemgetter(1), reverse=True):
#   print >>fout, pair[0]+'\t'+str(pair[1])

fout.close()


