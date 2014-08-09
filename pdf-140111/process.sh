#/usr/bin/sh

cd "$(dirname $0)/";
ROOT_PATH=`pwd`

mkdir output-$1

~/k2pdfopt-mac -ui- -w 2160 -h 3840 -odpi 300 $1.pdf
gs -dBATCH -dNOPAUSE -sDEVICE=png16m -dGraphicsAlphaBits=4 -dTextAlphaBits=4 -r300 -sOutputFile=./output-$1/page-%d.png $1_k2opt.pdf
