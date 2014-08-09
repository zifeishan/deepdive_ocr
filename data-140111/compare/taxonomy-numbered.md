Taxonomy of Knowledge
====

Numbers are manually sampled from 545 cases, where 505 (92.66%) are
solvable with automatic knowledge.

- Knowledge
  - Automatic knowledge (92.66%)
    - OCR-specific knowledge
      - Agreed assumption
        - If OCR outputs agree with each other, the output is correct
      - character-level
        * [twchar	7.71%] If Tesseract output have letter in {', ?, ", -}, it is wrong
        * [cwchar	3.12%] If Cuneiform output have letter in {', :, >}, it is wrong
      - word-level
        - [upp	3.67%] Upper/lower bound:
          * If output has changes from lower case to upper case, then it is wrong
          * If output has a similar proportion of lower-case letters and upper-case letters, then it is wrong
        * [charuni	3.12%] A word should only consist of letters, numbers, or special characters. A combination of those should be wrong.
        * [comb	13.58%] Combinability: if combination can generate candidate, current output should be wrong
        * [url	0.55%] URLs starts with "http" or "www" and can contain rare characters.

      - Sentence level
        - Upper / lower case 
          * [dot	2.57%] A dot (.) should not be followed by a lower-case letter
          * [upper	0.73%] A general word should be upper-case only if it is in the first word in sentence.
      - Document level
        - OCR accuracy on this document
          * [ocrdocacc	0.00%] OCR accuracy is dependent on document. Need this prior probability.

    - Corpus statistics
      - character-level
        - character frequency
          * [statc	0.18%] Rare characters should not appear 
        - character Ngram frequency
          * [statcgram	0.18%] Rare character combinations should not appear
      - word-level
        - [sw	47.89%] word frequency: in whole corpus / in this document
            * A word with high frequency is correct
            * A word with low frequency is wrong

        - [swgram	9.36%] word Ngram frequency (in whole corpus / this document)
          * A word Ngram with high frequency is correct
          * A word Ngram with low frequency is wrong

      - sentence-level
        - sentence frequency
          * [stats	0.00%] A sentence of high frequency is correct 
          
    - [d	38.90%] Dictionary
      * A word in dictionary is correct
      * A word not in dictionary is wrong

    - NLP
      - POS
        - [pos	1.47%] Single-word POS 
          - Word-POS dictionary
            * If the word have the POS in dictionary then it is correct
            * If the word do not have the POS in dictionary then it is wrong
          - Word-POS frequency in corpus
            * If word-POS combination is rare in corpus then it is wrong
        - POS-ngram frequency in corpus
          * [posgram	0.00%] if a POS-ngram is rare, then at least one of its words is wrong
      - Named entity recognition
        - Word-NER frequency in corpus
          * [ner	2.20%] If a word-NER combination is rare in corpus then it is wrong
        - NER-specific
          * [number	0.00%] If a word consist of numbers and dashes, it is a valid number.
          * [persondot	0.73%] Person name can come with ".", and this dot does not end a sentence
          * [by	1.10%] BY should follow a PERSON. (may change NER)
          * [etal	0.18%] et al should be followed by a PERSON.
      - Lemmatization
        * [lemma	0.00%] If lemma do not appear in dictionary, the word is wrong
      - Parsing
        - [path	1.10%] Dependency path corpus frequency
          * If all words in a path to root is frequent, all words on the path is correct
          * If all words in a path to root is rare, at least one word is wrong
          * If word Ngram on a path is frequent, these words is correct
    - Knowledge Base 
      - entity-level
        * [kbe	10.64%] If we can link a word to an entity in knowledge base, the word is correct
          - Freebase
          - Taxon
          - Location
          - Temporal
      - relation-level
        * [kbr	1.47%] If we can link two words to two entities and they have a relation, both of them are correct.

  - Human knowledge
    - Crowdsourced labels
    - Expert labels


- Rules to generate Candidates (?)
  - General Edit Distance
    * [ed	5.69%] Minimize edit distance to each option, while only generate candidate appearing in corpus / word-gram in corpus
  - OCR-specific Edit Rules
    * [edrule	6.42%] Weighted edit distance: some of the "edits" have small weights:
      - Tesseract "?" -> "fi"
      - Tesseract "?" -> "fl"
      - Tesseract "m" -> "rn"
      - Tesseract "nn" -> "rm"
      - Tesseract "]" -> "l"
      - Tesseract "|" -> "l"
      - Tesseract "?" -> "j"
      - Tesseract '?' -> '"'
      - Tesseract '"' -> '' (remove)
      - Tesseract '-' -> '' (remove)
      - Tesseract 'I-I' -> 'H'
      - Tesseract 'j' -> 'y'
      - Cuneiform "c" -> "e"
      - Cuneiform ":" -> '' (remove)
      - Tesseract '5' -> 'S'
      - Cuneiform '5' -> 'S'  - Weights are adjusted globally and document-specifically
      - Tesseract '?' -> 'e' (for other language)
      - Tesseract 'I' -> '1'
      - Cuneiform 'l' -> '1'

  - Segmentation manipulation
    * [comb	13.58%] Combine words to generate new candidate if they are in a same box
    * [seg	4.95%] Split words:
      - Split words to match dictionary / corpus
      - Split Tesseract words by '-'
      - Split words by removing any letter
    * [rmchar	7.71%] Remove rare characters


----


Future ways to generate new candidates:
- How to auto-learn rules & weights in document?
  - If number of words that rule f(A)=B can be applied in document, then rule f can be applied with high confidence?


Question: 
- Positive + negative rules?

- the vision OCR should consider font similarity: a != ll because if it is ll the should be larger
- Remove white spaces: compare all pages of a document. They should be same in white space area. 

- References: make use of titles?
- How to detect references?


<!--
Discarded rules:
* [numconf	0.37%] if Tesseract and Cuneiform output different numbers, Tesseract is correct and Cuneiform is wrong. 
-->


Assessment: get initial numbers!

Just get leaf probabilities!

- In an independent fashion; enumerate the conjunctions (combinations)
- Come up with a MIDDLE LAYER!

- Do a non-overlapping version, to fix the gaps.

- OCR-specific only
- Corpus-statistics -> Dict -> NLP -> Knowledge base incremental
- OCR-specific plus full incremental

