Protocol for OCR error analysis
====

**Dataset**: We assume that documents can be roughly classified into 3 classes according to OCR quality: clean, medium and dirty. We randomly choose one document from each class (3 documents in total), and we pick random pages from them to do error analysis. The number of real words in documents on which we do error analysis are: 2529 (clean), 715 (medium), 365 (dirty).

**Errors**: We define errors as words in document where at least 1 OCR do not give the correct output.  

**Rules**: Rules are leaf nodes in our knowledge taxonomy. There are two kinds of rules: (1) to judge whether a candidate is correct for a word, and (2) to generate a set of new candidates for a word.  We define that *a set of rules R can fix an error*, if the correct output can be judged by a combination of rules in *R*.

**Annotations**: In our dataset, OCR outputs are aligned by word, and we provide annotation for each word in our dataset. We annotate:

- For each OCR output, whether it is correct or not.
- For each error, what the correct word is.
- For each error, whether the error is fixable by automatic rules.
- If fixable, enumerate any possible combinations of rules in our knowledge taxonomy that can fix the error.


**Measurement**: Using the set of documents annotated, we compute the quality of our extractors. 

-	**OCR precision**: the fraction of correct outputs among all outputs by this OCR.
-	**OCR recall**: the fraction of correct outputs among all real words in the document.
-	**Error correction rate** for a ruleset *R*: the fraction of errors that can be fixed by at least one possible combination of rules in *R*.
-	**Forward search** for a ruleset *R*: the error correction rate for ruleset *R*.
-	**Lesion analysis** for a ruleset *R*: the error correction rate for ruleset *K - R*, where *K* is the whole set of rules in knowledge taxonomy.
