import sys
sys.path.append('..')
from preprocess import *

if __name__ == "__main__": 
  datc = CuneiReader.ReadURL('http://hazy.cs.wisc.edu/hazy/share/zifeipdf/13033.1/cuneiform-page-0001.html', 1)
  print len(datc)
  for word in datc:
    # print 'CONTENT:', word.GetContent()
    # print 'BOX:',  [(b.GetPage(),b.GetBoxes()) for b in word.GetBoxes()]
    # print 'SENTID:', word.GetSentId()
    # print word.GetAllParts()

    print('%s'%word.GetContent()),

    # raw_input()
  # print datt
  sys.exit(0)
