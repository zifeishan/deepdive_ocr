import sys
from preprocess import *
from pyquery import PyQuery
import re

def AlignAll(url, output_base):
  trytime = 0
  while (trytime < 3):
    try:
      pq = PyQuery(url = url)
      break
    except KeyboardInterrupt:
      raise KeyboardInterrupt
    except:
      print 'Timeout!', url
      trytime += 1

  lines = pq.find('a').text().split(' ')
  lines = [l.rstrip('/') for l in lines if re.match('[0-9].*', l)]

  for filename in lines:
    urlbase = 'http://hazy.cs.wisc.edu/hazy/share/zifeipdf/' + filename+'/'
    tessurl = urlbase +'input.text'
    curlbase = urlbase + 'cuneiform-page-'
    curlend = '.html'
    outputbase = output_base+filename
    Align.AlignFromURL(urlbase, outputbase)

if __name__ == "__main__": 
  if len(sys.argv) == 2:
    url = sys.argv[1]
  else:
    print 'Usage:',sys.argv[0],'<urlbase>'
    url = 'http://hazy.cs.wisc.edu/hazy/share/zifeipdf/'
    print 'Use default URL:', url

  AlignAll(url, '../../data/')
