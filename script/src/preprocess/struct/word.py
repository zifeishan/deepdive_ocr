from box import *
import re

class Word:

  def __init__(self):
    self._content = ''
    self._pos1 = ''
    self._pos2 = ''
    self._stem = ''
    self._pos3 = ''
    # There might be multiple boxes.
    self._somenumber = 0
    self._sentid = 0
    self._boxes = []

    self._alter = ''

  def AddBox(self, box):
    self._boxes.append(box)
  def SetContent(self, content):
    self._content = content
  def GetBoxes(self):
    return self._boxes
  def GetContent(self):
    return self._content
  def GetSentId(self):
    return self._sentid
  def GetAllParts(self):
    return [self._content, self._pos1, self._pos2, self._stem, self._pos3, self._somenumber, self._sentid, self._boxes]

  # TODO Only support two OCRs, add a char from cuneiform to this.
  # Accumulate a character to the alternative.
  def AddAlterChar(self, char):
    self._alter += char

  def GetSentId(self):
    return self._sentid

  def GetAlter(self):
    return self._alter

  # difference between original Tesseract output:
  # no WID; one more "alterative" content. (cuneiform output)
  def GetAllParts(self):
    parts = [
      self._content, 
      self._alter, 
      self._pos1, 
      self._pos2, 
      self._stem, 
      self._pos3, 
      self._somenumber, 
      self._sentid, 
      [b.GetPrinted() for b in self._boxes]
    ]
    return parts


# parts: as in Tesseract format
def NewWord(parts):
  word = Word()
  word._content = parts[1]
  if word._content == '':
    return word
  word._pos1 = parts[2]
  word._pos2 = parts[3]
  word._stem = parts[4]
  word._pos3 = parts[5]
  word._somenumber = int(parts[6])
  word._sentid = int(parts[7].lstrip('SENT_'))
  boxes = parts[8].rstrip(',').split(',')  # might be multiple boxes. Newline.
  boxes = [b.lstrip('[').rstrip(']') for b in boxes]

  # if len(boxes) > 1:
  #   print boxes, word._content, wid
  #   print parts

  for tmp in boxes:
    # tmp = boxes[0]
    # print tmp, parts[8]
    tbox = re.split('[pltrb]', tmp)
    # print tbox
    box = Box()
    box.SetPage(tbox[1])
    box.SetBoxes(tbox[2:])
    word.AddBox(box)

  return word
