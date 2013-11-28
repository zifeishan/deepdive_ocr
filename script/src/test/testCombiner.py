import sys
sys.path.append('..')
from preprocess import *

if __name__ == "__main__": 
  print 'Loading Tesseract...'
  filename = '13033.1'
  urlbase = 'http://hazy.cs.wisc.edu/hazy/share/zifeipdf/' + filename+'/'

  twords = TessReader.ReadURL(urlbase +'input.text')

  print 'Processing Tesseract...'

  curlbase = urlbase + 'cuneiform-page-'
  curlend = '.html'

  index = Combiner.BuildBoxIndexByPage(twords)
  succ_fail = [0, 0]
  for pagenum in sorted(index.keys()):
    pagestr = '%04d' % pagenum
    url = curlbase + pagestr + curlend

    print 'Loading Cuneiform Page', pagenum
    cchars = CuneiReader.ReadURL(url, pagenum)
    print 'Processing Cuneiform Page', pagenum
    this_sc = Combiner.Combine(twords, cchars, index)
    for i in range(0,2): 
      succ_fail[i] += this_sc[i]
  
  ## Test indexing
  # tsub = 0
  # for page in sorted(index.keys()):
  # # for page in range(1, len(index)+1):
  #   print 'PAGE:',page
  #   for bwpair in index[page]:
  #     if bwpair[1].GetContent() != twords[tsub].GetContent():
  #       print '  ', bwpair[0].GetBoxes(),'\t', bwpair[1].GetContent(),'\t',twords[tsub].GetContent()
  #       raw_input()
  #     tsub += 1
  

  # aligned, AGREED, miss_cuni, miss_tess
  stat = [0, 0, 0, succ_fail[1]]

  print 'Printing results...'
  fout = open('diff-'+filename+'.txt', 'w')
  for word in twords:
    linechar = ' '
    content = word.GetContent()
    alter = word.GetAlter()
    if alter == '':
      linechar = '.'
      stat[2] += 1
    elif content == alter:
      linechar = ' '
      stat[1] += 1
      stat[0] += 1
    else:
      linechar = 'X'
      stat[0] += 1
    print >>fout, '%s %20s %20s' % (linechar, word.GetContent(), word.GetAlter(), ), [b.GetPrinted() for b in word.GetBoxes()]
    # if word.GetAlter() == '':
    #   raw_input()
  fout.close()


  print 'Alignment SUCC/Fail:', succ_fail
  print 'STAT: aligned, AGREED, miss_cuni, miss_tess(wrong):'
  print '\t'.join(['%5d %.4f' % (s, float(s)/len(twords)) for s in stat])
  print 'Recall:', float(succ_fail[1]) / sum(succ_fail)

        
