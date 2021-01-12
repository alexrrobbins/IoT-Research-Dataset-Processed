#!/usr/bin/env python3

last_line = ''
write_last_line = True

infile = open("../ProcessedAttributes/Xbee_Combined_Report.txt", 'r')
outfile = open("../ProcessedAttributes/Xbee_Combined_Data.txt", "w")
line = True
while line:
    line = infile.readline()
    if not line[0].isdigit():
        last_line = line
        write_last_line = True
    else:
        if write_last_line:
            outfile.write(last_line)
        outfile.write(line)
        write_last_line = False

infile.close()
outfile.close()
