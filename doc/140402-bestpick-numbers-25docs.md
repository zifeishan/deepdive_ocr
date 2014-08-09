# Optimal Choices between Tesseract and Cuneiform

We compute the optimal solution to choose between Tesseract and Cuneiform on a small dataset, and see how much it can improve Tesseract.

## Protocol

### Model

Each document contains a ordered sequence of variables.

Each variable is defined by a set of overlapping boxes. Each variable has several candidates that indicate outputs.

Each candidate contains a sequence of words. Only one candidate can be picked in one variable as final output. Candidates are distinct. Currently one variable contains at most 2 candidates (given by Tesseract and Cuneiform) and each candidate can contain several words.

### evaluation metrics

We basically use evaluation metrics [defined here](https://www.assembla.com/spaces/paleodeepdive/documents/bg4mh6Mher44kBacwqEsg8/download/bg4mh6Mher44kBacwqEsg8). namely:

- **Evaluation approach:** find maximum sequence matching between Tesseract output and HTML.
	- O = #words in Tesseract
	- H = #words in HTML
	- M = #words that matches
	- **Precision** = M / O
	- **Recall** = M / H
	- Y's **Error reduction** on X: (Recall_Y - Recall_X) / (1 - Recall_X)

We adopt the results in [this error analysis](https://www.assembla.com/spaces/paleodeepdive/wiki/Error_analysis_OCR_evaluation_Mar_20_2014), namely removing all Figures and Tables, removing references, and fixing HTML tags.

What's different here is that we adopt **a stricter version** of evaluation based on one more assumption: For each candidate, we force its words to be adjacent in the mapping to supervision document. e.g, in the following case:

    cats dogs --> cats and dogs

Word `cats` and `dogs` cannot be mapped into `cats and dogs` since they are not adjacent there. We force the mapping to be strict among words inside a candidate.

### Objective

- We pick candidates that optimize the Recall ( M / H ).
- We compute Macro/Micro statistics: 
	- Macro: avg(M / H). 
	- Micro: sum(M) / sum(H).

## Experiment

### Experiment dataset

**25 documents**: (JOURNAL_) 121182, 67347, 36525, 154781, 151005, 69454, 46221, 168710, 6056, 159914, 90045, 53832, 40039, 145413, 75610, 69310, 99727, 14250, 118233, 107511, 12307, 83457, 59869, 28971, 14255

### Result

- On average, Optimal choice improve Tesseract Recall by **1.16% (Macro)** / 1.13% (Micro), and the error reduction rate is **13.20% (Macro)** / 12.05% (Micro).
- On average, Tesseract recall is **90.33% (Macro)** / 90.60% (Micro).
- On average, optimal recall is **91.49% (Macro)** / 91.73% (Micro).

- See following Figures (documents sorted by Tesseract recall):

### Comparing with Manual Error Analysis

These results are not very coherent with our initial manual error analysis:

- Tesseract Recall:
	- 97.07% (clean)	93.43% (medium)	77.26% (dirty)	89.25% (average)
- Optimal recall when picking from Tesseract / Cuneiform: 
	- 99.49% (clean)	95.24% (medium)	82.19% (dirty)	92.31% (average)
	- *(coming from "#Words where all OCRs fail")*
- Recall Improvement: 
	- 2.42% (clean)	1.81% (medium)	4.93% (dirty)	3.06% (average)
- Error Reduction:
	- 82.59% (clean)	27.55% (medium)	21.68% (dirty)	28.47% (average)

The reasons might be:
- strict evaluation decreases the recall
- alignment: initial error analysis align Cuneiform outputs to Tesseract outputs.
