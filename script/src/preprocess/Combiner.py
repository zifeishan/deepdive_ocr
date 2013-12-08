from util import *
import re

# Return a index of each page: index{1:[(b1,w1), (b2,w2)...], 2:[b10,b11..]}
# The list is sorted by Box comparator.
# If one word contains multiple boxes, they will be ALL indexed to the SAME word object.
def BuildBoxIndexByPage(words):
  index = {}
  for w in words:
    boxes = w.GetBoxes()
    for b in boxes:
      p = b.GetPage()
      if p not in index:
        index[p] = []
      index[p].append((b, w))  # page P, add a pair: box B, word W

  # for p in index:
  #   index[p].sort() # Sort the list for every page, based on box ULRD.

  return index

def GetNextSub(sub, maxsub):
  sub = sub + 1
  if sub >= maxsub:
    sub = 0
  return sub


def IsSingleMark(string):
  if len(string) != 1:
    return False
  return re.match("^[A-Za-z0-9]*$", string)  # Anything but letters and chars


# combine cchars into twords, stored in "Word" object!
def Combine(twords, cchars, index=None):
  if index == None:
    index = BuildBoxIndexByPage(twords)

  page = -1  # assume cchars are all in a same page (no problem if not)
  maxsub = 0
  last_sub = 0  # Start from sub 0

  succ_fail = [0, 0]
  # Try to align each character to a box.
  for char in cchars:

    # Suppose there is only ONE box for the character
    mybox = char.GetBoxes()[0]

    tpage = mybox.GetPage()
    if tpage != page: 
      page = tpage
      maxsub = len(index[page])
      last_sub = 0
      # print 'Processing Page:', page

    isStarting = False
    sub = last_sub

    aligned = False
    
    while sub != last_sub or isStarting == False:
      isStarting = True
      pair = index[page][sub] 
      box = pair[0]
      word = pair[1]
      if box.Contain(mybox):  # char is contained in this box

        # Special case: 
        # Words and marks can have SAME box in Tesseract.
        # Therefore it is very hard to align.
        # We assume in this case they are close to each other, and 
        nextsub = GetNextSub(sub, maxsub)
        nextbox = index[page][nextsub][0]
        nextword = index[page][nextsub][1]

        # Assume that one word has at most 2 boxes. 
        # There is a case that [b1,b2] [b1,b2] are continuous
        # e.g.
        # X                    (          (Cam-bridge ['P12,1919 2474 1984 2501', 'P12,1410 2506 1475 2532']
        # .            Cambridge                      ['P12,1919 2474 1984 2501', 'P12,1410 2506 1475 2532']
        if not nextbox.Equal(box):  # Try the next-next one
          nnsub = GetNextSub(nextsub, maxsub)
          nnbox = index[page][nnsub][0]
          nnword = index[page][nnsub][1]
          if nnbox.Equal(box):
            nextsub = nnsub
            nextbox = nnbox
            nextword = nnword

        if nextbox.Equal(box): # same box, the case might happen
          accumulated = word.GetAlter()
          wordtext = word.GetContent()

          # Case 1: exact match already
          # Case 2: equal length, non-alphabet left, next same.
          # VERY-LOOSE match: as long as LENGTH are equal!
          # assumption: they will NOT neglect characters.
          if (wordtext == accumulated) or (\
            len(wordtext) == len(accumulated) 
            # and nextword.GetContent() == char.GetContent() 
            # and IsSingleMark(char.GetContent())
            ):
            # Match to next word!
            sub = nextsub
            word = nextword
          # else nothing happens, still match to this word

        word.AddAlterChar(char.GetContent())
        aligned = True
        break

      # Not match, next sub.
      sub = GetNextSub(sub, maxsub)

    last_sub = sub  # update to the latest sub found. 
    # Worst case: O(n) for each iteration, 
    # n is number of words in a document.


    if not aligned:
      # print 'Fail to align char:', char.GetContent(), mybox.GetBoxes(), 'P:', page
      # print 'Last Word aligned:', index[page][last_sub][1].GetContent()
      # raw_input()
      succ_fail[1] += 1
    else:
      succ_fail[0] += 1

  return succ_fail






  # lasttword = None
  # lastcbox = None
  # cindex = 0
  # tindex = 0
  # newcdata = []
  # newtdata = []
  # emptyword = {CONTENT: '', BOX: { PAGE: 0, UP: 0, DOWN: 0, LEFT: 0, RIGHT: 0}}
  # # crm = []
  # # trm = []

  # while cindex < len(cdata) and tindex < len(tdata):
  #   tword = tdata[tindex]
  #   cword = cdata[cindex]
  #   cbox = cword[BOX]

  #   # Print(cword)
  #   # Print(tword)
  #   # print ''

  #   if cindex == 0:
  #     newcdata.append(cword)
  #     newtdata.append(tword)
  #     cindex += 1
  #     tindex += 1
  #     continue

  #   lasttword = newtdata[len(newtdata) - 1]
  #   lastcbox = newcdata[len(newcdata) - 1][BOX]

  #   lastcword = newcdata[len(newcdata) - 1]

  #   # Handle '-' line-breaking
  #   # Currently: only combine cdata.
  #   if lastcword[CONTENT].endswith('-') and BoxAbove(lastcbox, cword[BOX]):
  #     # Combine this cword into last in result
  #     newcdata[len(newcdata) - 1][CONTENT] = lastcword[CONTENT].rstrip('-') + cword[CONTENT]
  #     cindex += 1
  #     continue

  #   # todo boxcontain?
  #   # Tword is contained by last cword. Combine tword with last tword
  #   # Assumption: combine if "equal boxes"
  #   if BoxEqual(lastcbox, tword[BOX]):
  #     # print 'Combine', lasttword[CONTENT], tword[CONTENT]
  #     # raw_input()

  #     # Combine content
  #     newtdata[len(newtdata) - 1][CONTENT] += tword[CONTENT]
  #     # Do not add this tdata

  #     # lasttword[CONTENT] += tword[CONTENT]
  #     # trm.append(tword)
  #     tindex += 1
  #     continue

  #   # No combination cases
  #   else: 
  #     # Box not equal; not combined
  #     if not BoxEqual(tword[BOX], cword[BOX]):
  #       if BoxBefore(tword[BOX], cword[BOX]):
  #         # print 'tword before cword', tindex, cindex
  #         newcdata.append(emptyword)
  #         newtdata.append(tword)
  #         tindex += 1
  #       elif BoxBefore(cword[BOX], tword[BOX]):
  #         # print 'cword before tword', tindex, cindex
  #         newcdata.append(cword)
  #         newtdata.append(emptyword)
  #         cindex += 1
  #       else: 
  #         newcdata.append(cword)
  #         newtdata.append(tword)
  #         cindex += 1
  #         tindex += 1
  #     else:  # Match
  #       newcdata.append(cword)
  #       newtdata.append(tword)
  #       cindex += 1
  #       tindex += 1  
  #   # raw_input()
  
  # # TODO crm??? align while finding removelist??
  # # for w in trm: 
  # #   tdata.remove(w)

  # return newcdata, newtdata