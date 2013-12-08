Taxonomy of Knowledge
====

Features to choose between options
----

* Word-level features (same as former LR features)
  - WL(i): Word length.
  - Occur(i): Number of Search result on Internet.
  - DictValid(i): whether option i is valid in dictionary.
  - UpperPunish(i) = -4x(x-1), where x is upper case percentage in the
    option. The idea is that the percentage of upper-case characters in
    a word should be either near 0% or 100%.
  - LowerToUpperChange(i): how many times in the option is a lowercase
    character followed by an uppercase character.
  - Count of each character occurrence
  - Count of occurrence of two consequent character
  - POS(i): i's Part-of-speech tag.

* Lexical level
  - A window of k words to the left of i (including i)
    - e.g. for current word "dinosaurs" with a left window "the
      evolution of", check how many times "the evolution of dinosaurs"
      appear in our knowledge base (or maybe in this document / the
      corpus?)
  - A window of k words to the right of i (including i)
  - A window of k words' POS tags to the left of i including POS of i.
    - e.g. "PER VERB LOC" often appears in our knowledge base, but "NOUN
      NOUN NOUN" seldom appears.
  - A window of k words' POS tags to the right of i including POS of i

  - One idea is that we do not want one error to affect its neighboring
    words' tag patterns. e.g ABCDE, if B is wrong, 'BCD' tag pattern
    will also be invalid for word C even C is correct.
    - Maybe choose k = 1, 2, 3... as different features.

* Syntactic level
  - Dependency parse (not quite clear about how this works. Need
    discussion.)

* Semantic level
  - Understanding the relationship in this sentence (using relation
    extraction method).
    - Using both lexical and syntactic (dependency parse) features?
    - e.g. If our knowledge base contains a "place_found" relationship
      between Dinosaurs and "Wisconsin", we can be quite sure about the
      whole following sentence is correct:
      - "Dinosaurs was found in Wisconsin."

* Cross-sentence level
  - According to the locality of words, I assume that similar words
    should appear in near sentences, or through the whole document.

  - Word occurrence in a window of sentences
    - "If this word has appeared recently, it is likely to be correct?"
    - This factor connects multiple variables across sentences: words
      with same outputs are connected.

* Cross-document level
  - (Not quite sure)
  - If we assume all the documents are in a same domain, we can make use
    of word distribution, etc, in this domain.


How to make Suggestions
----

We may need to train another statistical model, to learn rules for
making suggestions. Not sure whether it needs one pass before the
classification, or they should go on simultaneously.

There are two ways to suggest words: based on knowledge of OCRs, and
based on knowledge of the content.

* OCR based:
  - For each variable if output-T is correct and output-C is wrong, it
    indicates that we can make a "suggestion" to output-C according to
    output-T.

  - Character-level
    - we have the knowledge what mistakes do OCR make in character
      level. e.g. when Tesseract outputs "m" it is often actually "ni".
      So for Tesseract with output "m" we may correct it to "ni".
    - Make a variable for each different character (or character
      combinations)

  - Word-level
    - Consider a window of characters before and after the variable.

* Content based:

  - Word-level
    - Consider the validness of the fixed word (similar to above
      features for classifier)

  - Semantic level
    - Make use of the knowledge base to suggest word.
    - e.g. If our knowledge base contains a "place_found" relationship
      between Dinosaurs and "Wisconsin", we can do correction to
      following cases:
      - "D???saurs was found in Wisconsin": Since we can detect a
        "founded" relation here, and we can match "what is found in
        Wisconsin" and find "Dinosaurs" similar to the first missing
        word.
      - "Dinosaurs was found in ?iscons???": Since we can detect a
        "founded" relation here, and we can match "Where are Dinosaurs
        found" and find "Wisconsin" similar to the last word.
      - "Dinosaurs w?s fo??? ?n Wisconsin": Since we know the Dinosaurs
        and Wisconsin pair are in our database, we match patterns
        similar to the sentence and found "was found in" is likely to be
        in the middle, thus correcting it.

  - Cross-sentence level
    - According to the locality of words, assume that similar words
      should appear in near sentences, or through the whole document.
    - Word occurrence in a window of sentences:
      - If a "correct" word X has appeared recently, and the current
        word can be modified to X within short modification distance,
        then it is likely to suggest word X in replacement of the
        current word.
