import datetime
import pandas as pd
import csv
import json
def make_url(ticker_symbol,start_date, end_date):
	base_url = "http://ichart.finance.yahoo.com/table.csv?s="
	# print ticker_symbol
	a = start_date
	b = end_date
	dt_url = '%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv'% (ticker_symbol, a.month-1, a.day, a.year, b.month-1, b.day,b.year)
	return base_url + dt_url

def getMarketMovers():
	L = ["aapl","axp","ba","cat","csco","cvx","ko","dd","xom","ge","gs","hd","ibm","intc","jnj","jpm","mcd","mmm","mrk","msft","nke","pfe","pg","trv","unh","utx","v","vz","wmt","dis"]
	
	day = (datetime.datetime.now() - datetime.timedelta(hours=9,minutes=30)).day	
	s = datetime.date(2017,3,day-1)
	e = datetime.date(2017,3,day)
	D = {}
	for i in L:
		print i
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


	
	# keys = s[0].keys()
	with open('backup_stuff/market_movers.csv', 'wb') as output_file:
		for item in s:
			up_down = 0
			if item[1] < 0:
				up_down = -1
			else:
				up_down = 1
			output_file.write(str(item[0])+","+str(up_down)+"\n")
	return s
		

if __name__ == '__main__':
	print getMarketMovers()
