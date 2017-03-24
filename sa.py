import pandas as pd
import numpy as np

def do_sentiment_analysis(string):
	hash_table = dict()
	litigious = pd.read_csv('files/litigious.csv', header = 0)
	negative = pd.read_csv('files/negative.csv', header = 0)
	positive = pd.read_csv('files/positive.csv', header = 0)
	uncertain = pd.read_csv('files/uncertain.csv', header = 0)

	litigious = litigious.values
	negative = negative.values
	positive = positive.values
	uncertain = uncertain.values
	
	for a in string:
		# print a
		a = a.upper()
		if a in hash_table:
			if (hash_table[a] < 0):
				hash_table[a]=hash_table[a] - 1
			else:
				hash_table[a]=hash_table[a] + 1
		elif a in negative:
			hash_table[a]=-1
		elif a in positive:
			hash_table[a]=1
	
	# print (hash_table.values())
	sentiment_value = sum(hash_table.values())
	return sentiment_value

if __name__ == '__main__':
	string = ["Reliance","Capital","abused","sell","the","stake","it","has","in","Paytm","to","Chinese","e-commerce","giant","Alibaba","Group","for","Rs","275","crore","","sources","privy","to","the","development","tell","CNBC-TV18.","Reliance","Capital","had","invested","Rs","10","crore","to","acquire","its","stake","in","the","payment","and","e-commerce","company","and","retains","it","free","of","cost","In","the","latest","fund","raising","round","Paytm","was","valued","at","USD","1","billion.","China's","Alibaba","Group","and","affiliate","Ant","Financial","are","the","largest","shareholders","of","One97","Communications","","the","parent","company","of","Paytm","and","have","a","stake","close","to","around","40","percent"]
	do_sentiment_analysis(string)
