Error analysis new:
1. ??? output, -- correct
2. liverpool vs Liverpool
3. { vs (
4. 标反了！！！！！

New features:
1. 字母数字共同出现



http://hazy.cs.wisc.edu/demo/paleo/pdf/4968.2
http://hazy.cs.wisc.edu/demo/paleo/pdf/29644
http://hazy.cs.wisc.edu/demo/paleo/pdf/15291
http://hazy.cs.wisc.edu/demo/paleo/pdf/551.2
http://hazy.cs.wisc.edu/demo/paleo/pdf/32360.2
http://hazy.cs.wisc.edu/demo/paleo/pdf/16179.2
http://hazy.cs.wisc.edu/demo/paleo/pdf/16689
http://hazy.cs.wisc.edu/demo/paleo/pdf/43229
http://hazy.cs.wisc.edu/demo/paleo/pdf/13960
http://hazy.cs.wisc.edu/demo/paleo/pdf/6815.2
http://hazy.cs.wisc.edu/demo/paleo/pdf/4968


Can you start from these documents? You can find their PDF in these link, and their corresponding NLP files at 

madmax:/lfs/madmax/0/czhang/paleopaleo/input_large

Analysis
====

4968.2: 

- Tesseract word-alignment wrong, consider box combine.

29644:

- "-" inside words can be cancelled (character-remove)
- Character-modify rules + neighbor-combine + dictionary should work well!

Tesseract generate additional chars: how remove?
"

./,: next char Upper/lower

. + Upper case: shallow, sentense-level