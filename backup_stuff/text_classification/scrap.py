from goose import Goose
import requests
from bs4 import BeautifulSoup
import lxml
import datetime

def stockQuery(stockSymbol):
	""" Returns a table with various information about a stock"""
	stockSymbol = stockSymbol.upper()
	end_date = datetime.date.today()
	start_date = datetime.date.today() - datetime.timedelta(days=2)
	seed_url = "https://www.google.com/finance/company_news?q="+stockSymbol+"&ei=kT3SWJGvNMeguASQ3K7wCw&startdate="+str(start_date)+"&enddate="+str(end_date)+"&start=1&num=15"
	#seed_url1="https://www.google.com/finance/company_news?q=AAPL&ei=kT3SWJGvNMeguASQ3K7wCw&startdate=2017-03-21&enddate=2017-03-23&start=1&num=15"
	return_list = []
	

	r = requests.get(seed_url)
	soup = BeautifulSoup(r.content,'lxml')
	url_list = soup.find_all('a', id='n-cn-')

	for url in url_list:
		table = {'title': None, 'text': None, 'img_url': None, 'url': None, 'publish_date': None}
		url = url['href']
		url = url[url.find('url=')+4:url.find('&cid')]
		
		g = Goose()
		article = g.extract(url=url)

		try:
			title = article.title
			table['title'] = title 
		except Exception, e:
			table['title'] = ""

		try:
			text = article.cleaned_text
			table['text'] = text
		except Exception, e:
			table['text'] = ""

		try:
			img = article.top_image.src
			table['img_url'] = img
		except Exception, e:
			table['img_url'] = ""

		try:
			article_url = article.final_url
			table['url'] = article_url
		except Exception, e:
			table['url'] = url

		article_date = article.publish_date

		if article_date != None:
			if len(article_date) > 19:
				if article_date[19] == '+' or 'Z':
					time_hour = int(article_date[11:13])
					if time_hour < 4:
						time_hour = time_hour + 20
						date = int(article_date[8:10]) - 1
						article_date = article_date[:8] + str(date) + article_date[10:]
					else:
						time_hour = time_hour - 4

					if time_hour < 10:
						article_date = article_date[:11] + '0' + str(time_hour) + article_date[13:]	
					else:
						article_date = article_date[:11] + str(time_hour) + article_date[13:]

				article_date = article_date[:19]
		
		
		table['publish_date'] = article_date
		return_list.append(table)
		print "Scraped Article ",len(return_list),"\tCompany: ",stockSymbol,"\tTitle: ",table['title']

		if(len(return_list) == 2):
			return return_list	





