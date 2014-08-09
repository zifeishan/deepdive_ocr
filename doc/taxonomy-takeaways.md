- Actual #words in document
- #Words in OCR output
  - Tesseract
  - Cuneiform
- #Words where all OCRs fail
- **Errors**: #words in document where at least 1 OCR make errors
- #Errors that can be solved using rules (automatically solvable)
- OCR Accuracy
- OCR recall on document
- OCR recall on errors (#errors that each OCR get correct output)

- Top-5 recall single knowledge on errors (forward search)
  - for judging between candidates
    - Corpus statistics of single words (sw)
    - General-purpose dictionary of correct words (d)
    - Corpus statistics of single words (swgram)
    - Entity-level knowledge in KB (kbe)
  - for generating candidates
    - seg
    - comb
    - rmchar
    - edrule
    - ...?

- Lesion of knowledge with top-5 highest recall reduction on errors
  - for judging between candidates
  - for generating candidates


- Knowledge recall in different taxonomies
  - OCR Specific (twchar, cwchar, upp, charuni, comb, url, dot, upper)
  - Corpus Statistics & Dictionary (d, sw, swgram, statc)
    - on single words (d,sw,statc)
    - on N-gram of words (swgram)
  - NLP (pos,ner,number,persondot,lemma,path,by,etal)
  - Knowledge Base (kbe,kbr)


TODO!!!