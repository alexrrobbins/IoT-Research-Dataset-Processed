#!/bin/bash
#echo "PCAP Infile: "
#read infile
#echo "Outfile: "
#read outfile
input_filter="./display_filters.txt"
infile="./Xbee_Normal.pcap"
outfile="./Xbee_Normal_Report.txt"
sleep 5

while IFS= read -r line
do
                                                                                                                              
	tshark -r $infile -T fields -e $line -E bom=y -E header=y -E separator=, -V >> $outfile
	 
done < "$input_filter"

grep "\S" $outfile > "../ProcessedAttributes/Xbee_Normal_Report.txt"
