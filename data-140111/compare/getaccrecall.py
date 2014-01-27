#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def TCPrinter(arr, stream):
  print >>stream, '  Tesseract:', arr[0]
  print >>stream, '  Cuneiform:', arr[1]

def ParseRuleComb(rulecomb):
  return tuple(sorted(rulecomb.split('+')))

def EncodeRuleComb(ruletuple):
  return '+'.join(ruletuple)

if __name__ == "__main__": 
  if len(sys.argv) == 2:
    path = sys.argv[1]
  else:
    print 'Usage:',sys.argv[0],'<SingleFile>'
    sys.exit(1)

  lines = [l.strip(' \n') for l in open(path).readlines()]

  tot_doc = 0       # For recall
  diff_doc = 0      # For recall on disagreed outputs
  tot_ocr = [0, 0]  # For acc
  non_correct = 0   # Both OCR fails
  correct = [0, 0]  # OCR results
  diff_correct = [0, 0]  # OCR results on disagreed words
  solved = 0        # If apply all rules, how many correct answers recalled



  tags = [l.strip() for l in open('rule-tags.md').readlines()]
  
  # This map gives an UPPER BOUND for: only using this rule, how many correct answers recalled
  know_tot = {t:0 for t in tags}  

  # This map gives an UPPER BOUND for: only using this rule, how many correct answers out of the DISAGREED 
  know_disagree = {t:0 for t in tags}  

  # This map gives an UPPER BOUND for: only using this rule, how many correct answers out of the DISAGREED 
  know_noncorrect = {t:0 for t in tags}  

  # This is a dict: for each knowledge, if removed, how many words are lost. (recall lost)
  tag_lesion = {t:0 for t in tags}

  for l in lines:
    
    if l == '':  # empty line
      continue

    if '///' in l:
      l = l.replace('///', '|||')

    w1 = l[3:18].strip(' ')   # TODO: what if too long?
    w2 = l[19:19+15].strip(' ')

    l = l.split('|||')
    # print l

    if len(l) < 2:  # agreed
      tot_doc += 1
      for i in (0,1):
        tot_ocr[i] += 1
        correct[i] += 1
      for sol in know_tot: 
        know_tot[sol] += 1  # all solutions can solve it
      continue

    args = [p.strip(' ') for p in l[1].split('$')]
    # sol_str = [s.strip() for s in args[0].split(',')]
    sol_str = args[0]
    answers = args[1:]

    if len(answers) == 0:  # no mark, ignore this word.
      continue

    # Count this word.
    if w1 != '': 
      tot_ocr[0] += 1
    if w2 != '': 
      tot_ocr[1] += 1

    this_num = 0
    if len(answers) == 1 and answers[0] == '':  # this is not a word, no recall
      this_num = 0
    else:
      this_num = len(answers)

    tot_doc += this_num
    diff_doc += this_num

    this_non_correct = False

    if answers[0] == '1':  # T correct
      correct[0] += this_num
      diff_correct[0] += this_num
    elif answers[0] == '2':  # C correct
      correct[1] += this_num
      diff_correct[1] += this_num
    else:
      non_correct += this_num
      this_non_correct = True

    if w2 == '' and sol_str == '' and answers[0] in ['', '1']:  # auto-pick...
      sol_str = 'd,sw'
    # ASSUMPTION: IF ONLY ONE HAS OUTPUT, it should be trivial to get $1 or $ right.
    # JUST USE d + sw for all of them.

    # print 'Solutions:',sol_str,'\tAnswers:',answers

    # examine solutions
    sols = [p.strip(' ') for p in sol_str.split(',')]

    if '?' in sol_str:  # cannot be solved with automatic knowledge
      sols = []           # no solutions

    if len(sols) > 0:
      solved += this_num
    # else:
    #   print 'Unsolvable:',sol_str

    for sol in sols:
      if sol not in know_tot:
        if sol == '': continue
        # print sol
        unknown = False
        comb = ParseRuleComb(sol)  # May be a combination. tuple of the combination.
        print comb
        for k in comb:
          if k not in know_tot:
            unknown = True
        
        if unknown:
          continue
        else:
          sol = EncodeRuleComb(comb)
          know_tot[sol] = 0
          know_disagree[sol] = 0
          know_noncorrect[sol] = 0

      know_tot[sol] += this_num
      know_disagree[sol] += this_num
      if this_non_correct:
        know_noncorrect[sol] += this_num

    # Lesion analysis
    # Get "sets" of rules--comb of tags
    sets = [{s for s in ParseRuleComb(s)} for s in sols]
    if len(sets) > 0:
      essential = sets[0]
      for ss in sets:
        essential.intersection_update(ss)

      for tag in essential:
        if tag == '': continue
        tag_lesion[tag] += this_num




  fout = open('stats/'+path+'.stat.txt', 'w')
  print diff_doc, tot_doc, tot_ocr, correct, non_correct


  print >>fout, 'Total document words:',tot_doc
  print >>fout, ''

  print >>fout, 'Total OCR output words:'
  TCPrinter(tot_ocr, fout)
  print >>fout, ''

  print >>fout, 'OCR correct outputs:'
  TCPrinter(correct, fout)
  print >>fout, ''

  print >>fout, 'Words where all OCRs fail:',non_correct, '(%.4f%%)' % (non_correct*100.0 / tot_doc)
  print >>fout, ''

  print >>fout, 'Accuracy:'
  TCPrinter(['%.4f%%' % (100.0 * correct[i] / float(tot_ocr[i])) for i in (0,1)], fout)
  print >>fout, ''

  print >>fout, 'Recall on total document:'
  TCPrinter(['%.4f%%' % (100.0 * correct[i] / float(tot_doc)) for i in (0,1)], fout)
  print >>fout, ''

  print >>fout, 'Words where at least 1 OCR make errors (disagreed / agreed but both failed):',diff_doc, '(%.4f%%)' % (100.0 * diff_doc / float(tot_doc))

  print >>fout, 'Automatically solvable errors:', solved, '(%.4f%%)' % (100.0 * solved / float(diff_doc))
  print >>fout, ''

  print >>fout, 'Recall on error (disagree / both fail) words:'
  TCPrinter(['%.4f%%' % (100.0 * diff_correct[i] / float(diff_doc)) for i in (0,1)], fout)
  print >>fout, ''


  import pprint
  pp = pprint.PrettyPrinter(indent=2) # pretty printer

  # print >>fout, '\nRecall for each knowledge on all words:'
  # for s in ['%10s: %.4f%%' % (t, know_tot[t] / float(tot_doc) * 100.0 )
  #     for t in sorted(know_tot, key=know_tot.get, reverse=True)]:
  #   print >>fout,'  '+s

  print >>fout, '\nRecall for each knowledge on error words:'
  for s in ['%10s: %.4f%%' % (t, know_disagree[t] / float(diff_doc) * 100.0 )
      for t in sorted(know_disagree, key=know_disagree.get, reverse=True)]:
    print >>fout,'  '+s

  print >>fout, '\nRecall for each knowledge on words where OCRs all fail:'
  for s in ['%10s: %.4f%%' % (t, know_noncorrect[t] / float(non_correct) * 100.0 )
      for t in sorted(know_noncorrect, key=know_noncorrect.get, reverse=True)]:
    print >>fout,'  '+s

  print >>fout, '\nLesion for each knowledge on error words:'
  for s in ['%10s: %.4f%%' % (t, tag_lesion[t] / float(diff_doc) * 100.0 )
      for t in sorted(tag_lesion, key=tag_lesion.get, reverse=True)]:
    print >>fout,'  '+s

  fout.close()

