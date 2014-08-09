cut -f 2 *.output.txt.compare.txt | sort | uniq -c | sort -fnr > grep-stat.tmp
python getstat.py grep-stat.tmp