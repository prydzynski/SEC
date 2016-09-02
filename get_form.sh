#!/bin/bash

echo "Enter the year you wish to access: "
read year
echo "Enter the QTR you wish to access[1-4]: "
read qtr
qtr="QTR$qtr"

query="ftp://ftp.sec.gov/edgar/full-index/$year/$qtr/form.idx"
out_file="./forms/$year/"$qtr"form.idx"

if [ -f "$out_file" ]
then
        echo "File already exists! Would you like to over write [y/n]: "
        read overwrite
        if [[ "$overwrite" == "y" ]]
        then
                rm $out_file
                wget -O $out_file --user=anonymous --password='email@email.com' $query;
        else
                exit 113
        fi
else
        wget -O $out_file --user=anonymous --password='email@email.com' $query
fi
