import csv

file = open('out.csv','r')
re = csv.reader(file)
for row in re:
	print row[0]