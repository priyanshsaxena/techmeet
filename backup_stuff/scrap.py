from goose import Goose
import requests
from bs4 import BeautifulSoup
import lxml
import datetime
from unidecode import unidecode
import feedparser
import data_processing as dp
def stockQuery(stockSymbol):
	""" Returns a table with various information about a stock"""
	stockSymbol = stockSymbol.upper()
	f = open("backup_stuff/sources")
	source = f.readlines()[0]

	up_down = {}
	market_movers_file = open("backup_stuff/market_movers.csv")
	lines = market_movers_file.readlines()
	for line in lines:
		line = line.split("\n")[0]
		c_sym,c_upDown = line.split(",")
		up_down[c_sym] = c_upDown


	stockSymbol = stockSymbol.upper()
	end_date = datetime.date.today() - datetime.timedelta(hours=9,minutes=30)
	start_date = end_date - datetime.timedelta(days=2)
	seed_url = source+stockSymbol+"&ei=kT3SWJGvNMeguASQ3K7wCw&startdate="+str(start_date)+"&enddate="+str(end_date)+"&start=1&num=100&output=rss"
	#seed_url1="https://www.google.com/finance/company_news?q=AAPL&ei=kT3SWJGvNMeguASQ3K7wCw&startdate=2017-03-21&enddate=2017-03-23&start=1&num=15"
	return_list = []
	d = feedparser.parse(seed_url)
	e = d['entries']

	for item in e:
		article = {}
		#article['time'] = item['published_parsed']
		article['url'] = unidecode(item['link'])
		article['title'] = unidecode(item['title'])
		bs = BeautifulSoup(item['summary'])
		text = unidecode(bs.text)
		x = text.split("\n")
		article['text'] = x[len(x)-2]
		
	# r = requests.get(seed_url)
	# soup = BeautifulSoup(r.content,'lxml')
	# url_list = soup.find_all('a', id='n-cn-')

	# for url in url_list:
	# 	table = {'title': None, 'text': None, 'img_url': None, 'url': None, 'publish_date': None}
	# 	url = url['href']
	# 	url = url[url.find('url=')+4:url.find('&cid')]
		
		# Extracting article text
		g = Goose()
		g_art = g.extract(url=article['url'])

	 	try:
			text = g_art.cleaned_text
			if len(text)>10:
				article['text'] = text
		except Exception, e:
			pass

	# 	try:
	# 		img = article.top_image.src
	# 		table['img_url'] = img
	# 	except Exception, e:
	# 		table['img_url'] = ""

		# if article is relevant append
		# up_down = 0
		r = dp.relevancy_of_article(stockSymbol , article['text'], up_down[stockSymbol.lower()])
		if(r==1):
			return_list.append(article)
			print "Scraped Article ",len(return_list),"\tCompany: ", stockSymbol,"\tTitle: ", article['title']
		else:
			print "Article found irrelevant by SVM, finding more"
		if(len(return_list)==10):
			break

	return return_list


if __name__ == '__main__':
	stockQuery("GE")


