import sys
sys.path.append('..')
from preprocess import *

if __name__ == "__main__": 

  filename = '13033.1'
  urlbase = 'http://hazy.cs.wisc.edu/hazy/share/zifeipdf/' + filename+'/'
  tessurl = urlbase +'input.text'
  curlbase = urlbase + 'cuneiform-page-'
  curlend = '.html'
  outputbase = 'output/'+filename
  Align.AlignFromURL(urlbase, outputbase)
