#!/bin/bash

echo "Enter the name of the file you wish to parse (ex. forms/year/qtrform.idx): "
read filename
path=$(dirname "${filename}")
infile=$(basename "${filename}")
qtr=${infile:0:4}
outfile="$path/"$qtr"_cik.csv"
echo ":$outfile:"

while true
do
        if [ -f "$outfile" ]
        then
                echo "Outfile already exists! Would you like to overwirte [y/n]: "
                read overwrite
                if [[ $overwrite == "y" ]]
                then
                        >$outfile
                        break
                elif [[ $overwrite == "n" ]]
                then
                        break
                else
                        "Invalid entry!\n"
                fi
        else
                break
        fi
done

echo "Enter the file type you would like to extract (ex. 10-K): " 
read filetype
filetype="$filetype "
length=${#filetype}

while read line;
do 
        substring=${line:0:$length}
        if [[ $substring == $filetype ]] ;
        then
                echo $line >> $outfile 
        fi
done < $filename
