for filename in `ls tmp/*.png`; do
        DOCID=${filename%.png};
    convert -density 750 $filename $DOCID.ppm
    tesseract $DOCID.ppm $DOCID.hocr hocr
    rm $DOCID.ppm
done