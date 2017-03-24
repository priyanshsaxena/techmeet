# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pysentiment as ps
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def stemming(tokenized_docs_no_stopwords):
	wnl = WordNetLemmatizer()
	porter = PorterStemmer()
	snowball = SnowballStemmer('english')
	wordnet = WordNetLemmatizer()
	preprocessed_docs = []

	final_doc = []
	for doc in tokenized_docs_no_stopwords:
		final_doc.append(porter.stem(doc))
	return final_doc

def sentiment(text):
	hiv4 = ps.HIV4()
	score = hiv4.get_score(text)
	return score

def data_cleaning(text):
	tokenized_text = word_tokenize(text)
# ----------------------------------- Remove punctuation--------------------------------------------------------------------		
	regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html
	tokenized_text_no_punctuation = []
	new_review = []
	for token in tokenized_text:
		new_token = regex.sub(u'', token)
		if not new_token == u'':
			new_token = new_token.lower()
			new_review.append(new_token)
	tokenized_text_no_punctuation = new_review
 # -------------------------------------------- Remove stopwords ----------------------------------------------------------
	new_term_vector = []
	for doc in tokenized_text_no_punctuation:
	    if not doc in stopwords.words('english'):
	        new_term_vector.append(doc)
	    
	text_no_stopwords = new_term_vector
	text_no_stopwords = stemming(text_no_stopwords)
	# print (text_no_stopwords)
	return text_no_stopwords


def process(company_name , article):

# ----- check if company name is present ----------
	company_name = company_name.lower()
	fh_syn=open("companies.txt","r")
	list_company_names = fh_syn.read().split('\n')
	fh_syn.close()
	company_name_present = 0
	if company_name in list_company_names:
		company_name_present = 1

	article = data_cleaning(article)
	company_name = data_cleaning(company_name)
	score = sentiment(article)
	
	fh_syn=open("words.txt","r")
	list_of_relevant_words=fh_syn.read().split('\n')
	fh_syn.close()
	
	cnt = 0;
	for i in article:
		if i in list_of_relevant_words:
			cnt = cnt + 1
	cnt = float(cnt)/len(article)

	# form of ---> vector = [company_name_present , cnt , polarity , positive , negative , subjectivity]
	vector = [company_name_present , cnt]
	score = score.values()
	vector.append(score[0])
	return vector

if __name__ == '__main__':
	company_name = "McDonalds"
	head_lines = "Discerning Google Stock Is as Simple as a Trend Line"
	article = "Google!!! simple walking profiling stock$  has^!@#%%^&**(())_  been,  a great.  performing investment susan"
	vector = process(company_name , article)			
