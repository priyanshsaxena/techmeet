import datetime
import pandas as pd

def make_url(ticker_symbol,start_date, end_date):
	base_url = "http://ichart.finance.yahoo.com/table.csv?s="
	# print ticker_symbol
	a = start_date
	b = end_date
	dt_url = '%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv'% (ticker_symbol, a.month-1, a.day, a.year, b.month-1, b.day,b.year)
	return base_url + dt_url

def getMarketMovers(day):
	L = ["aapl","axp","ba","cat","csco","cvx","ko","dd","xom",
	"ge","gs","hd","ibm","intc","jnj","jpm","mcd","mmm","mrk","msft","nke","pfe","pg","trv","unh","utx","v","vz","wmt","dis"]

	s = datetime.date(2017,3,day)
	e = datetime.date(2017,3,day+1)
	D = {}
	for i in L:
		u =  make_url(i,s,e)
		# print u

		data = pd.read_csv(u).values
		open_ = data[0][1]
		close_ = data[0][4]
		percent_change = (close_ - open_)/open_
		# print data
		# print percent_change
		D[i] = percent_change

	s = []
	for key, value in sorted(D.iteritems(), key=lambda (k,v): (v,k)):
		# print "%s: %s" % (key, value)
		s.append([key,value])
	return s
		

if __name__ == '__main__':
	getMarketMovers(21)
