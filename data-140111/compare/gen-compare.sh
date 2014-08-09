python generate_compare.py $1 $2
python modify_compare.py $1.compare.txt
mv $1.compare.txt.mod $1.compare.txt
