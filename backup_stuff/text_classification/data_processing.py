# Author - Neha M (IIT Mandi)
# Processing the news article and generating a vector which can be given as input to the SVM model

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
from sklearn.externals import joblib

# --------------- Remove stemming from the tokenized article ----------------
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

# ---------------- sentiment analysis of the news article ------------------
def sentiment(text):
	hiv4 = ps.HIV4()
	score = hiv4.get_score(text)
	return score

def data_cleaning(text):
	tokenized_text = word_tokenize(text)
# --------------- Remove punctuation from text-----------------------------		
	regex = re.compile('[%s]' % re.escape(string.punctuation)) 
	tokenized_text_no_punctuation = []
	new_review = []
	for token in tokenized_text:
		new_token = regex.sub(u'', token)
		if not new_token == u'':
			new_token = new_token.lower()
			new_review.append(new_token)
	tokenized_text_no_punctuation = new_review

 # ---------------------- Remove stopwords from text----------------------
	new_term_vector = []
	for doc in tokenized_text_no_punctuation:
	    if not doc in stopwords.words('english'):
	        new_term_vector.append(doc)
	    
	text_no_stopwords = new_term_vector
	text_no_stopwords = stemming(text_no_stopwords)
	return text_no_stopwords


def process(company_sym , article, up_down):
	D = {"aapl":["apple"],"axp":["american express"],"ba":["boeing"],"cat":["caterpillar"],"csco":["cisco"],"cvx":["chevron"],"ko":["coca-cola","coca cola"],"dd":["dupont","du pont"],"xom":["exxon"],"ge":["general electric"],"gs":["goldman sachs","gs", "goldmansachs","goldman-sachs"],"hd":["home depot"],"ibm":["ibm"],"intc":["intel"],"jnj":["Johnson & Johnson","J&J"],"jpm":["jpmorgan","jp morgan","j p morgan", "j.p. morgan"],"mcd":["mcdonalds","mcd"],"mmm":["3m"],"mrk":["merck"],"msft":["microsoft"],"nke":["nike"],"pfe":["pfizer"],"pg":["procter & gamble","p&g"],"trv":["travelers"],"unh":["united health"],"utx":["united technologies"],"v":["visa"],"vz":["verizon"],"wmt":["walmart"],"dis":["disney"]}
	print company_sym
	company_sym = company_sym.lower()
	
	list_company_names = D[company_sym]
	for i in list_company_names:
		x = " " + i + " "
		article = " " + article + " "

	# ----- check if company name is present in article----------------------
		company_name_present = 0
		if x in article:
			company_name_present = 1

#--------clean the article before sentiment analysis---------------------
	article = data_cleaning(article)
	score = sentiment(article)

#---------look for distinct relevant words in the article-----------------
	fh_syn=open("words.txt","r")
	list_of_relevant_words=fh_syn.read().split('\n')
	fh_syn.close()

	hash_table = dict()	
	cnt = 0;
	for i in article:
		if i in hash_table:
			continue;
		elif i in list_of_relevant_words:
			cnt = cnt + 1
			hash_table[i] = 1
	cnt = float(cnt)/len(article)

# form of ---> vector = [company_name_present , cnt , polarity , positive , negative , subjectivity]
	vector = [company_name_present , cnt]
	score = score.values()
	vector.append(score[0] * up_down)
	return vector


def relevancy_of_article(company_symbol , article, up_down):
	
	vector = process(company_symbol, article, up_down)
	clf = joblib.load('svm_model.pkl')
	predictedlabel = clf.predict(vector) 
	return predictedlabel[0]

if __name__ == '__main__':
	company_name = "Gori"
	up_down = 1
	fh_syn=open("xyz","r")
	article = fh_syn.read()
	fh_syn.close()
	predictedlabel = relevancy_of_article(company_name, article, up_down)		
	# print (predictedlabel)