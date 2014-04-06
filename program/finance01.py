import nltk
import csv

dataReader = csv.reader(open(067_Hiashi.csv, 'rb'), deliminator=' ', quotechar='|')

for(row in dataReader):
	print','.join(row)
