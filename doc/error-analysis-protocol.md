NEW TODO

Learn Denny's language

Error analysis on new critical PDFs.

- OCR Error Analysis / Evaluation Protocols / Objectives

  - Alignment
    - How many words are detected by each OCR?
    - How many words are aligned (detected by all/both OCRs)?
    - Segmentation Accuracy of aligned words
    - How many words are only detected by one (not all) OCR?
    - Segmentation Accuracy of words only detected by one OCR
    
  - OCR Errors
    - Accuracy / Error rate of each OCR: correctly detected words / all words in a document
    - Accuracy / Error rate of each OCR when OCRs do not agree
      - Based on assumption: when OCRs agree, their results are correct.
        - Check this assumption by hand-labeling, distantly-supervising these results.
    - How many times at least one OCR is correct?

  - Human baseline
    - How many times human can recover the correct spelling by only looking at the OCR results?
    - How many times human can recover the correct spelling if he reads the whole sentence/document?

- Previous Experiment Result:
  - Corpus statistics
    - Number of papers: 3
    - Number of words in total (given by Tesseract): 21,641
    - Number of aligned words: 21,652
    - Number of words that OCRs do not agree: 1,011
    - Hand-labeled words: all 1,011 words where OCRs do not agree; no labels for words that OCRs agree.

  - OCR Results
    - Accuracy of each OCR over all aligned words:
      - Tesseract: 97.60%
      - Cuneiform: 97.00%
    - Accuracy of each OCR over disagreed words:
      - Tesseract: 48.66%
      - Cuneiform: 35.71%
    - How many times at least one OCR is correct, over disagreed words:
      - 84.37%
    - Assumption (agreed outputs are correct): UNCHECKED

  - Human results:
    - How many times human can recover the correct spelling by only looking at the OCR results?
      - TODO
    - How many times human can recover the correct spelling if he reads the whole sentence/document?
      - TODO

  - Machine Learning results 
    - Accuracy when choosing among 3 classes -- Tesseract / Cuneiform / Neither:
      - Accuracy of Logistic Regression (learning rate = 0.015): 76.23%
      - Accuracy of SVM (linear kernel): 84.08%
    - Definite Accuracy of different Classifiers in terms of output text, over disagreed words:
      - SVM: 75.77%
      - Cuneiform: 35.71%
      - Tesseract: 48.66%





========


  * Justify word-level segmentation by error analysis
Learn Denny's language

Encode Simple LR in Denny's language 



Also, before you do any error analysis, can you write down the protocol? For example, what statistics are we seeking. I can think about some (but I am sure there are more!):

These numbers are important for our story (paper) and our road map (system) to proceed. (They are actually more important than what ML model we use :-) They are the insight and novelty that we will bring to the community, and we are the only people who can bring them in.) So lets make sure we are on the same page on them.



Also, think about how can you collect these statistics--Can we deploy some of them to geoscientists (they have multiple students), can we deploy some of them of Turkers, what interface do we need to build to make them efficient (and therefore save your time for annotation), how many examples we need to collect to make statistically-sound claim, how can we control human-errors and noises during annotation?

You do not need to come-up with answers for all of them, but just keep them in mind when you making your todo and write down the protocol :-)
