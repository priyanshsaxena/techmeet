# -*- coding: utf-8 -*-
import pysentiment as ps

def sentiment(text):
	hiv4 = ps.HIV4()
	tokens = hiv4.tokenize(text.decode('utf-8'))
	score = hiv4.get_score(tokens)
	print (score)

if __name__ == '__main__':
	string = ""
	sentiment(string)	
