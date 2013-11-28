import sys
sys.path.append('..')
from preprocess import *

if __name__ == "__main__": 
  datt = TessReader.ReadURL('http://hazy.cs.wisc.edu/hazy/share/zifeipdf/13033.1/input.text')
  print len(datt)
  for word in datt:
    print 'CONTENT:', word.GetContent()
    print 'BOX:',  [(b.GetPage(),b.GetBoxes()) for b in word.GetBoxes()]
    print 'SENTID:', word.GetSentId()
    print word.GetAllParts()

    if len(word.GetBoxes()) > 1:
      raw_input()
  # print datt
  sys.exit(0)
