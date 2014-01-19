Taxonomy of Knowledge
====

- Knowledge
  - Automatic knowledge
    - OCR-specific knowledge
      - Agreed assumption
        - If OCR outputs agree with each other, the output is correct
      - character-level
        * [twchar] If Tesseract output have letter in {', ?, ", -}, it is wrong
          - e.g. (......)
        * [cwchar] If Cuneiform output have letter in {', :, >}, it is wrong
        
      - word-level
        * [upp] If output has changes from lower case to upper case, then it is wrong
        * [upp] If output has a similar proportion of lower-case letters and upper-case letters, then it is wrong
        * [charuni] A word should only consist of letters, numbers, or special characters. A combination of those should be wrong.
        * [comb] Combinability: if combination can generate candidate, current output should be wrong
        <!-- * [numconf] if Tesseract and Cuneiform output different numbers, Tesseract is correct and Cuneiform is wrong. -->
        * [url] URLs starts with "http" or "www" and can contain rare characters.

      - Sentence level
        - Upper / lower case 
          - [dot] A dot (.) should not be followed by a lower-case letter
          - [upper] A general word should be upper-case only if it is in the first word in sentence. (?)
      - Document level
        - OCR accuracy on this document
          * [ocrdocacc] OCR accuracy is dependent on document. Need this prior probability.

    - Corpus statistics
      - character-level
        - character frequency
          * [statc] Rare characters should not appear 
            - (> twchar + cwchar?)
        - character Ngram frequency
          * [statcgram] Rare character combinations should not appear
      - word-level
        - word frequency: in whole corpus / in this document
            * [sw] A word with high frequency is correct
            * [sw] A word with low frequency is wrong

        - word Ngram frequency: in whole corpus / in this document
          * [swgram] A word Ngram with high frequency is correct
          * [swgram] A word Ngram with low frequency is wrong

      - sentence-level
        - sentence frequency
          * [stats] A sentence of high frequency is correct 
          
    - Dictionary
      * [dict] A word in dictionary is correct
      * [dict] A word not in dictionary is wrong

    - NLP
      - POS
        - Word-POS dictionary
          * [pos] If the word have the POS in dictionary then it is correct
          * [pos] If the word do not have the POS in dictionary then it is wrong
        - Word-POS frequency in corpus
          * [pos] If word-POS combination is rare in corpus then it is wrong
        - POS-ngram frequency in corpus
          * [posgram] if a POS-ngram is rare, then at least one of its words is wrong
      - Named entity recognition
        - Word-NER frequency in corpus
          * [ner] If a word-NER combination is rare then it is wrong
          * [number] If a word consist of numbers and dashes, it is a valid number.
          * [persondot] Person name can come with ".", and this dot does not end a sentence
          * [by] BY should follow a PERSON. (may change NER)
          * [etal] et al should be followed by a PERSON.
      - Lemmatization
        * [lemma] If lemma do not appear in dictionary, the word is wrong
      - Parsing
        - Dependency path corpus frequency
          * [path] If all words in a path to root is frequent, all words on the path is correct
          * [path] If all words in a path to root is rare, at least one word is wrong
          * [path] If word Ngram on a path is frequent, these words is correct
    - Knowledge Base 
      <!-- available at: http://fossilworks.org/bridge.pl -->
      - entity-level
        * [kbe] If we can link a word to an entity in knowledge base, the word is correct
          - Freebase
            - e.g.
                           (               (   CD NUMBER  
                          P.              P.  NNP      O  
                    echimzta        ectzinat   FW      O  |||comb,ed,kbe
                           )              a)   FW      O  |||(echinata)

          - Taxon
            - e.g. 
                Galerapygus     Galeropygus   NN      O
                correct: Galeropygus
          - Location
          - Temporal
      - relation-level
        * [kbr] If we can link two words to two entities and they have a relation, both of them are correct.

  - Human knowledge
    - Crowdsourced labels
    - Expert labels


- Rules to generate Candidates (?)
  * [ed] Minimize edit distance to each option, while only generate candidate appearing in corpus / word-gram in corpus
  * [edrule] Weighted edit distance: some of the "edits" have small weights:
    * Tesseract "?" -> "fi"
    * Tesseract "?" -> "fl"
    * Tesseract "m" -> "rn"
    * Tesseract "nn" -> "rm"
    * Tesseract "]" -> "l"
    * Tesseract "|" -> "l"
    * Tesseract "?" -> "j"
    * Tesseract '?' -> '"'
    * Tesseract '"' -> '' (remove)
    * Tesseract '-' -> '' (remove)
    * Tesseract 'I-I' -> 'H'
    * Tesseract 'j' -> 'y'
    * Cuneiform "c" -> "e"
    * Cuneiform ":" -> '' (remove)
    * Tesseract '5' -> 'S'
    * Cuneiform '5' -> 'S'  - Weights are adjusted globally and document-specifically
    * Tesseract '?' -> 'e' (for other language)
    * Tesseract 'I' -> '1'
    * Cuneiform 'l' -> '1'
  * (How to auto-learn rules & weights in document?)
      - document-level
        - If number of words that rule f(A)=B can be applied in document, then rule f can be applied with high confidence (????)

  - Segmentation manipulation
    * [comb] Combine words to generate new candidate if they are in a same box
    * [seg] segment words to match dictionary / corpus
    * [seg] segment Tesseract words by '-'
    * [seg] segment words by removing any letter
    * [rmchar] Remove rare characters


  - e.g. Zc-o'logy, Zaokjgy. -> Zoology

Question: 
- Positive + negative rules?

- the vision OCR should consider font similarity: a != ll because if it is ll the should be larger
- Remove white spaces: compare all pages of a document. They should be same in white space area. 

- References: make use of titles?
- How to detect references?
 
Assessment: get initial numbers!

Just get leaf probabilities!

- In an independent fashion; enumerate the conjunctions (combinations)
- Come up with a MIDDLE LAYER!

- Do a non-overlapping version, to fix the gaps.

- OCR-specific only
- Corpus-statistics -> Dict -> NLP -> Knowledge base incremental
- OCR-specific plus full incremental
