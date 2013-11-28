import sys
from preprocess import *

# Assume a fixed URL base.
# Output alignment results in output_base.*
def AlignFromURL(urlbase, output_base):

  tess_url = urlbase +'input.text'
  curlbase = urlbase + 'cuneiform-page-'
  curlend = '.html'

  print 'Loading Tesseract from:', tess_url
  twords = TessReader.ReadURL(tess_url)
  print 'Processing Tesseract...'

  flog = open(output_base + '.log', 'w')

  index = Combiner.BuildBoxIndexByPage(twords)
  succ_fail = [0, 0]

  # for (url, pagenum) in cunei_urls:

  # Assume a fixed cuneiform URL format.
  for pagenum in sorted(index.keys()):
    pagestr = '%04d' % pagenum
    url = curlbase + pagestr + curlend
    print 'Loading Cuneiform Page', pagenum
    cchars = CuneiReader.ReadURL(url, pagenum)
    print 'Processing Cuneiform Page', pagenum
    this_sc = Combiner.Combine(twords, cchars, index)
    for i in range(0,2): 
      succ_fail[i] += this_sc[i]
  
  # aligned, AGREED, miss_cuni, miss_tess
  stat = [0, 0, 0, succ_fail[1]]

  print 'Printing results...'
  fout = open(output_base+'.diff.txt', 'w')
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


  print >>flog, 'Alignment SUCC/Fail:', succ_fail
  print >>flog, 'STAT: aligned, AGREED, miss_cuni, miss_tess(wrong):'
  print >>flog, '\t'.join(['%5d %.4f' % (s, float(s)/len(twords)) for s in stat])
  print >>flog, 'Recall:', float(succ_fail[1]) / sum(succ_fail)

  flog.close()        

  fout = open(output_base+'.output.txt', 'w')
  lastsentence = 1
  wid = 1
  for word in twords: 
    sid = word.GetSentId()
    if sid != lastsentence:
      lastsentence = sid
      wid = 1
      print >>fout  # println

    # Word ID + all other parts
    print >>fout, '\t'.join([str(p) for p in 
      ([wid] + word.GetAllParts())
      ])
    wid += 1

  fout.close()