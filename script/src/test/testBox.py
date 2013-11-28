import sys
sys.path.append('..')
from preprocess import *

b1 = Box()
b1.SetBoxes([1,2,3,4])
b2 = Box()
# print b2.GetBoxes()
b2.SetBoxes([4,2,3,1])
w1 = Word()
w2 = Word()
w1.AddBox(b1)
w2.AddBox(b2)
print w1.GetBoxes()[0].GetBoxes()
print w2.GetBoxes()[0].GetBoxes()
