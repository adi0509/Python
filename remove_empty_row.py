#This program reads in a .csv file called out.csv and removes all empty rows then creates a new file without the rows called FitBit.csv

import csv
input1 = open('out.csv', 'r')
output = open('FitBit.csv', 'w', newline='')
writer = csv.writer(output)
for row in csv.reader(input1):
    if any(row):
        writer.writerow(row)
input1.close()
output.close()
