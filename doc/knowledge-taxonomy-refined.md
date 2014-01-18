Taxonomy of Knowledge
====

- Knowledge
  - Automatic knowledge
    - OCR-specific knowledge
      - character-level
        * [twchar] If Tesseract output have letter in {', ?}, it is wrong
          - e.g. (......)
        * [cwchar] If Cuneiform output have letter in {', -}, it is wrong
        
      - word-level
        * [upperchange] If output has changes from lower case to upper case, then it is wrong
        * [upperpunish] If output has a similar proportion of lower-case letters and upper-case letters, then it is wrong

        - character unity
          * [charuni] A word should only consist of letters, numbers, or special characters. A combination of those should be wrong.
          * [dot] A dot (.) should not be followed by a lower-case letter


    - Corpus statistics
      - character-level
        - character frequency
          * [] Rare characters should not appear
        - character Ngram frequency
          * [] Rare character combinations should not appear
      - word-level
        - word frequency
          * [] A word with high frequency is correct
          * [] A word with low frequency is wrong
        - word Ngram frequency
          * [] A word Ngram with high frequency is correct

      - sentence-level
        - sentence frequency
          * [] A sentence of high frequency is correct
          
    - Dictionary
      * [] A word in dictionary is correct
      * [] A word not in dictionary is wrong

    - NLP
      - POS
        - Word-POS dictionary
          * [] If the word have the POS in dictionary then it is correct
          * [] If the word do not have the POS in dictionary then it is wrong
        - Word-POS frequency in corpus
          * [] If word-POS combination is rare in corpus then it is wrong
        - POS-ngram frequency in corpus
          * [] if a POS-ngram is rare, then at least one of its words is wrong
      - Named entity recognition
        - Word-NER frequency in corpus
          * [] If a word-NER combination is rare then it is wrong
      - Lemmatization
        * [] If lemma do not appear in dictionary, the word is wrong
      - Parsing
        - Dependency path corpus frequency
          - If all words in a path to root is frequent, all words on the path is correct
          - If all words in a path to root is rare, at least one word is wrong
    - Knowledge Base 
      <!-- available at: http://fossilworks.org/bridge.pl -->
      - entity-level
        * [] If we can link a word to an entity in knowledge base, the word is correct
          - Taxon
          - Location
          - Temporal
      - relation-level
        * [] If we can link two words to two entities and they have a relation, both of them are correct.

  - Human knowledge
    - Crowdsourced labels
    - Expert labels

- BY + ...(person)

- Rules to generate Candidates (?)
  * Tesseract "?" -> "fi"
  * Tesseract "?" -> "fl"
  * Tesseract "m" -> "rn"
  * Tesseract "nn" -> "rm"
  * Tesseract "]" -> "l"
  * Tesseract "?" -> "j"
  * Tesseract '?' -> '"'
  * Cuneiform "c" -> "e"
  * (How to auto-learn rules?)
      - document-level
        * [] If number of words that rule f(A)=B can be applied in document, then rule f can be applied with high confidence (????)



  - e.g. Zc-o'logy, Zaokjgy. -> Zoology

Question: 
- Positive + negative rules?

Assessment: get initial numbers!

Just get leaf probabilities!

- In an independent fashion; enumerate the conjunctions (combinations)
- Come up with a MIDDLE LAYER!

- Do a non-overlapping version, to fix the gaps.

- OCR-specific only
- Corpus-statistics -> Dict -> NLP -> Knowledge base incremental
- OCR-specific plus full incremental
