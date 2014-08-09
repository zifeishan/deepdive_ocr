# Experiment on Extractor Performance with Pypy / Python / Java

## Testing dimensions

Testing Application: OCR (naive feature extraction)

Database: (all GreenPlum)
- Rocky 64-frag databse
- Madmax4 8-frag database

Language:
- pypy
- python
- java

Protocol: 

count the time from `INFO  executing extractorName=ext_naivefeature` to `INFO  Completed task_id=ext_naivefeature with Success(Done!)`

Amount of Data:
- input: processing 29 documents, 603105 words in total
- output: extracted 786048 rows of features
- input batch size to extractors: default. (50000)

## Running with DeepDive

```
             Rocky     Madmax4
-------   --------  ----------
PYPY          43 s        40 s
PYTHON       136 s       152 s
JAVA          31 s        24 s
```

## Running without DeepDive

    PROGRAM   Madmax5
    -------   --------
    PYPY      39 s
    PYTHON    246 s
    JAVA      20 s

<!--
  ## With a Regex

    PROGRAM   Madmax5
    -------   --------
    PYPY      41 s
    PYTHON    246 s
    JAVA      21 s
 -->

## Running without DeepDive With 26 more Regexs (compiled on the fly):

    PROGRAM   Madmax5
    -------   ------------
    PYPY      71 s (39 + 32)
    PYTHON    246 s
    JAVA      44 s (20 + 22)

<!-- ## python script:

def time(s1, s2):
  d1 = datetime.strptime(s1, "%H:%M:%S")
  d2 = datetime.strptime(s2, "%H:%M:%S")
  print d2 - d1
 -->

## Conclusion

- Pypy is much faster than python (use pypy!)
- Java is less than 2x faster than pypy. 
- Java is not better than pypy in handling regex; Perl is good at regex.
