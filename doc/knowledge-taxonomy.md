Taxonomy of Knowledge
====

Dimensionality of Taxonomy
----

- tools / human
  - tools: OCR
  - human: experts, crowdsourcing
- entity / relation
  - entity: dict, web, domain-corpus..
  - relation: KB, ngram? parsing?
- character / word / sentence / document / corpus
- internal / external 
  - (dictionary / KB / other corpus, are external)
- structured / unstructured


Initial taxonomy
----

* Tool(OCR)-specific knowledge (?)
  - Single-tool knowledge
    + (specific correction rules: rm->nn, etc)
      + (weight dependent on document?)
  - Inter-tools knowledge ? (do we really have this?)
    + (correction rules within multiple ocrs) ?

* Human knowledge
  - Expert labeling
    + (a label is actually a rule)
  - Crowdsourced labels

* Linguistic features ??
  - (these are features, not corpus... features to extract->corpus to supervise. What are knowledge?)
  - Shallow NLP: POS
  - Deep NLP
    - dependency parse, 
    - named entity recognition

* Entity-level knowledge (a table of different hierarchies)
  - character level
    - character frequency
  - word level
    - word frequency in:
      - Linguistic dictionary
      - General corpus 
        - (Web)
      - Domain-specific corpus 
        - (Paleo documents)
      - This corpus (internal, cross-document)
  - sentence level
    - sentence frequency in: (same as above)

<!-- - internal / external ??? -->
<!-- - char/word/sent/doc/corpus level knowledges? -->

* Relation-level knowledge
  - relation among characters
    - char-gram
    - OCR-specific edit rules (overlap?)
  - relation among words
    - POS-gram
    - dependency parse
  - Structural knowledge base



Two tasks in this project
----
1. to generate new candidates
  - edit distance
  - Rules to "edit" can be learned in a tool-specific setting
2. to select a candidate
  - supervision and inference rules


Project architecture:
OCR, human <-> Candidates <-> 


Features to choose between options
----

* Character Level
  - Edit distance combined with dictionary
  - OCR-specific edit rules
  - Cross-word character combination / N-gram (fix bad segmentation)

* Word level
  - Shallow word-level features
  - Dictionary
    - Shallow English dictionary
    - General corpus (Web)
    - Domain-specific corpus (Paleo)
  - Cross-sentence word combination (fix bad segmentation)

  - POS(i): i's Part-of-speech tag.

* Document level
  - OCRs make similar errors within a single document!
  - 


* Lexical level
  - A window of k words to the left of i (including i)
    - e.g. for current word "dinosaurs" with a left window "the
      evolution of", check how many times "the evolution of dinosaurs"
      appear in our corpus / this document / whole
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


Feedback from Chris
====

One thing I really like is using the structured knowledge. For example, we know all the place names, the relationships that are likely to occur between fossils, taxa, etc. Can we use this to do a better job somehow? (Distributions over terms or over relationships?)

At one level this is exactly joint inference and learning: what we've been advocating over the last few years---it's a great general purpose tool and very powerful! (we use it everywhere)

We are exploring this problem in OCR because the "type" of information one gets from OCR (primarily visual features), the markup from NLP, and then the structured knowledge are all strong where the other is weak. We've been playing this game between NLP and structured knowledge, but we suspect that there are even larger gains if the signals are more "orthogonal"---that's why we are so interested in this test case.

Chris