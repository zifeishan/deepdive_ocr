# Error analysis: OCR evaluation (Mar 20, 2014) 

Currently Tesseract have only ~60% precision in our evaluation, which is
much lower than expected --- results in our previous manual error
analysis show that Tesseract should achieve 81.37% average precision and
89.25% recall. We examine the results to find why our evaluation metrics
is not coherent with our prior findings.

- **Experiment dataset:** 6 documents 
	- [JOURNAL_121182](http://www.sciencedirect.com/science/article/pii/S0921818111000658/pdfft?md5=785a95891d6553bfebb20b2041aa3886&pid=1-s2.0-S0921818111000658-main.pdf)
  - [JOURNAL_12307](http://www.sciencedirect.com/science/article/pii/S0031018210004803/pdfft?md5=919ad0d7f226393888e180a1f1f269c5&pid=1-s2.0-S0031018210004803-main.pdf)
  - [JOURNAL_145413](http://www.sciencedirect.com/science/article/pii/S0034666797000766/pdfft?md5=b3b0ab166415db975c9ed19ed0c4c06b&pid=1-s2.0-S0034666797000766-main.pdf)
  - [JOURNAL_59869](http://www.sciencedirect.com/science/article/pii/S0047248412000814/pdfft?md5=49b4c043dcf5a1c3943700d40521d71b&pid=1-s2.0-S0047248412000814-main.pdf)
  - [JOURNAL_6056](http://www.sciencedirect.com/science/article/pii/S1367912000000298/pdfft?md5=2c9b33cda3b65af51cb39b104bc8f681&pid=1-s2.0-S1367912000000298-main.pdf)
  - [JOURNAL_90045](http://www.sciencedirect.com/science/article/pii/S0895981199000267/pdfft?md5=2613a2848b42d5a8406370343e178aed&pid=1-s2.0-S0895981199000267-main.pdf)

- **Evaluation approach:** find maximum sequence matching between Tesseract output and HTML.
	- O = #words in Tesseract
	- H = #words in HTML
	- M = #words that matches
	- **Precision** = M / O
	- **Recall** = M / H

## Error 1: HTML tags (Recall + 4.51%)

We found that in results there are lots of HTML image tags such as:

		&lt;img class="figure large" border="0" alt="Full-size image (57 K)" src="http://origin-ars.els-cdn.com/content/image/1-s2.0-S0895981199000267-gr1.gif" data-thumbEID="1-s2.0-S0895981199000267-gr1.sml" data-fullEID="1-s2.0-S0895981199000267-gr1.gif"&gt; 

We remove these tags and look at the results again. We still evaluate on Tesseract original outputs. On average of 6 documents.

Average result:

- Precision: `57.92% -> 57.89%`
- Recall: `59.98% -> 64.49%`

Recall is improved by 4.51% on average. Precision goes down slightly.

## Error 2: Text inside Tables and Figures (Recall + 16.15%)

### Tables

On document [JOURNAL_90045](http://www.sciencedirect.com/science/article/pii/S0895981199000267/pdfft?md5=2613a2848b42d5a8406370343e178aed&pid=1-s2.0-S0895981199000267-main.pdf), there are lots of tables, even laying out vertically. In this document, Tesseract have precision 36.57% and recall 46.70%.  OCRs totally fail in vertical tables, and do badly on horizontal tables.

### Figures

We found that there are sometimes text inside images / Figures. ScienceDirect do not give their outputs inside figures, but give outputs to figure titles.

### Solution (together)

We ignore all figures and tables in HTML for evaluation. We also ignore all the table / figure captions (since some of them are also vertically aligned)

(in HTML, exclude all divs with class `figTblUpiOuter`)

Average result:

- Precision: `57.89% -> 52.48%`
- Recall: `52.48% -> 80.64%`

Recall goes up by 16.15% on average. Precision go down by 5,40%, since we did not exclude tables / figures in OCR outputs; it is non-trivial work.

For now we just use recall as evaluation metric.


## Error 3: Reference format (Recall + 10.91%)

In [JOURNAL_12307](http://www.sciencedirect.com/science/article/pii/S0031018210004803/pdfft?md5=919ad0d7f226393888e180a1f1f269c5&pid=1-s2.0-S0031018210004803-main.pdf), 
we can see that [HTML](http://www.sciencedirect.com/science/article/pii/S0031018210004803/) and [PDF](http://www.sciencedirect.com/science/article/pii/S0031018210004803/pdfft?md5=919ad0d7f226393888e180a1f1f269c5&pid=1-s2.0-S0031018210004803-main.pdf) varies slightly in reference format. 

ScienceDirect change reference format in PDF to maintain some coherency within its website, but it is not necessarily coherent with PDF. e.g. 

		PDF:                       Amiot, R., Lécuyer, C., ...
		HTML:  Amiot et al., 2004  R. Amiot, C. Lécuyer, ...

Besides, HTML has an additional link before all references, and in references they always put first name first, while in PDF it is not always the case.

Therefore, we **ignore all the references** in evaluation.

Average result:

- Precision: `52.48% -> 43.23%`
- Recall: `80.64% -> 91.55%`

We see that recall further goes up by 10.91% on average.  (Especially on the previous document we mentioned, JOURNAL_12307, recall increases by 20.24%) 

Precision goes down further by 9.26%, since re remove the whole reference section from HTML, but not change removing from OCR. Excluding references in OCR is also not trivial.

At last Tesseract outputs achieves **91.55% recall** on these 6 documents, which is coherent to our analysis with **medium to clean level documents**.

<!-- 

## Further errors

Quotation marks are different in PDFs and HTMLs: ‘’ and `'. There might be further slight differences, but the paragraphs
 -->

