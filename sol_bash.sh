#!/bin/bash
filename=$1
startpoint=`grep -nr "Voltage:" $1 | grep "Current:" | awk  '{print $1}' | sed "s/\://g"`
end=`awk -v s=$startpoint 'NF==1&&NR>s{print NR}' $1 | head -n 1`
echo $1 $end $filename
head -n $end $filename | awk -v s=$startpoint 'NR>s{print $1, $3}'  > curve.tmp
echo "ylabel='I'; xlabel='V';plot 'curve.tmp'"  | gnuplot -persist
