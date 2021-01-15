#!/usr/bin/env python3

# Some code taken from https://stackoverflow.com/questions/47519294/pandas-dataframe-read-csv-with-rows-that-have-not-have-comma-at-the-end
import pandas as pd
import io
import re
headers = []
unprocessed_dict = {}

# Extract headers from the text file
with open("../ProcessedAttributes/Xbee_Normal_Data.txt") as infile:
    data = infile.read() + '\n'
    headers = re.findall("wpan.*", data)
   # read_file = pd.read_csv(io.StringIO(data.replace(',','\n')),delimiter='\n',usecols=headers)
   # read_file.to_csv (r'../CSV/Xbee_Normal_Revised.csv',index=None)
    infile.close()

# Set up a dictionary using the headers as keys
for item in headers:
    unprocessed_dict.update({item : []})

# Read through the file again, adding all non-headings to the dictionary under their headings
with open("../ProcessedAttributes/Xbee_Normal_Data.txt") as infile:
 
    counter = 0
    data = infile.readline()
    while data and counter < len(headers):
        if not data[0].isdigit():
            counter += 1
            data = infile.readline()
        else:
            unprocessed_dict[headers[counter]].append(data)
            data = infile.readline()

# Pad dictionary lists with empty to avoid pandas error
# Code taken from https://stackoverflow.com/questions/40442014/python-pandas-valueerror-arrays-must-be-all-same-length
def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list

processed_dict = pad_dict_list(unprocessed_dict, ' ')

# Use Pandas to generate the CSV file
df = pd.DataFrame.from_dict(processed_dict, orient="columns")
df.to_csv("../CSV/Xbee_Normal_Test.csv")
