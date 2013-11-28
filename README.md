Deepdive OCR Project
====

This is the project repository for Deepdive OCR project, using ensemble
learning and distant supervision to combine multiple open-source OCRs to
a better one.


TODO (with tentative timelines)
====

1. Background reading: ACL' 12 (Nov 21)
  - distant supervision
  - dependency path for sentence-level correction

2. Preprocessing: re-implement alignment (Nov 24)
  - former implementation is based on Ce's intermediary output, and has some problems in alignment
  - we want to rewrite it to compromise speed for better alignment accuracy

3. Assumption verification: (Nov 24)
  - Our work has a current assumption that OCRs do word-level segmentation (detect spaces between words) correctly.
  - we will check the validity of this assumption after proper alignment.
  - check whether the space is detected correctly

4. Problem formalization: write a formal definition of our problem. (Nov 25)
  - Define words, inputs, outputs, knowledge, etc

5. Defining the taxonomy of different levels of knowledge (Nov 28)
  - Currently we have a vague definition: word-level, POS, sentense-level, cross-document.

6. Proposed model formalization: (Nov 30)
  - Write first draft of the proposed model to integrate multiple level of knowledge.

7. Implement initial model in Denny's language (Dec 4)

8. Experiments on different levels of knowledge: (Dec 8)
  - for each type of knowledge, give examples / error analysis of whether / why they should work

