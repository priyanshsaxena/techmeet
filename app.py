import csv
import json
from flask import Flask, render_template, request
import requests
import json
import sys
import stocks
import threading, webbrowser,random
sys.path.insert(0,"backup_stuff/")
import scrap as sra
import market_movers
app = Flask(__name__)

namemap = {"Apple":"aapl","American Express":"axp","Boeing":"ba","Caterpillar":"cat","Cisco":"csco","Chevron":"cvx","Coca-Cola":"ko","Dupont":"dd","Exxon":"xom","General Electric":"ge","Goldman Sachs":"gs","Home Depot":"hd","IBM":"ibm","Intel":"intc","Johnson & Johnson":"jnj","JP Morgan":"jpm","McDonalds":"mcd","3M":"mmm","Merck":"mrk","Microsoft":"msft","Nike":"nke","Pfizer":"pfe","Procter & Gamble":"pg","Travelers":"trv","United Health":"unh","United Technologies":"utx","Visa":"v","Verizon":"vz","Walmart":"wmt","Disney":"dis"}
articles = {}
arr = []

@app.route('/')
def index():
	bot1 = a[0][0]
	bot1value = a[0][1]
	bot2 = a[1][0]
	bot2value = a[1][1]
	top1 = a[29][0]
	top1value = a[29][1]
	top2 = a[28][0]
	top2value = a[28][1]
	for name, key in namemap.items():
		if(key==bot1):
			bot1full = name
		elif(key==bot2):
			bot2full = name
		elif(key==top1):
			top1full = name
		elif(key==top2):
			top2full = name
	arr = [bot1, bot2, top1, top2, bot1value, bot2value, top1value, top2value, bot1full, bot2full, top1full, top2full]
	for i in range(0,4):
		arr[i] = arr[i].upper()

	print arr
	return render_template('index.html', results=arr)

@app.route('/topics')
def topics():
	return render_template('topics.html')

@app.route('/process', methods=['POST'])
def process():
	query =  namemap[request.json[0:]]
	if not(query in cross):
		articles.update({query:sra.stockQuery(query)})
		cross.append(query)
	#print query
	info = stocks.getPrices(query)
	#print info
	for i in info:
		print i[0], type(i[0])
	allArticles = articles[query]
	return json.dumps({'company':request.json[0:],'resultsArray':info,'articleslist':allArticles})

@app.route('/search')
def search():
	return render_template('search.html')

if __name__ == '__main__':
	print "Running....."
	a = market_movers.getMarketMovers()
	cross = [a[0][0],a[1][0],a[29][0],a[28][0]]
	print "Part 1 done..."
	file = open('static/output.txt','wb')
	for i in cross:
		articles.update({i:sra.stockQuery(i)})
		ls = articles[i]
		file.write(i + '\n')
		for vals in ls:
			file.write(vals['title'] + '\n' + vals['url'] + '\n')
		print "------------"
	print "Firing UI...."
	file.close()
	app.run(debug = True, use_reloader=False)