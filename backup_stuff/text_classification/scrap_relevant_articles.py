import data_processing
import scrap
import stocks
import datetime
from unidecode import unidecode
def epochToEDT(epoch):
	return (datetime.datetime.fromtimestamp(epoch) - datetime.timedelta(hours=9,minutes=30))

def parse_publish_date(pub_date):
	
	if(pub_date.count("T")==1):
		date,time = pub_date.split("T")
	else:
		return None
	year,month,day = map(int,date.split("-"))
	hour,mint,sec = map(int,time.split(":"))
	return datetime.datetime(year=year,month=month,day=day,hour=hour,minute=mint,second=sec)

def binSearch(arr,item):
	top,size = 0,len(arr)
	while(top<size):
		mid = (top+size)/2
		if(arr[mid]==item):
			return mid
		elif arr[mid]>item:
			size = mid
		else:
			top = mid+1
	return top

def getArticles(sym):
	return_list = []
	prices = stocks.getPrices(sym)
	j = sym
	Times = [epochToEDT(x[1]) for x in prices]
	# item = epochToEDT(1490111745)
	# print item
	articles = scrap.stockQuery(j.upper())
	for i in articles:
		time = None
		text = unidecode(i['text'])
		title = i['title']
		url = i['url']
		img_url = i['img_url']
		print i['title'],i['publish_date']
		if i['publish_date'] is not None:
			time = parse_publish_date((i['publish_date']))
		else:
			print "Time not available"

		prediction = 0
		up_or_down = -1 
		if(time is not None):
			pos = binSearch(Times,time)
			
			if (prices[pos+10][4]-prices[0][4])>0:
				#stock moved up due to this news
				up_or_down = 1

			if(len(text)>10):
				prediction = data_processing.relevancy_of_article(j,text,up_or_down)
			print prediction
		else:
			
			# if (prices[30][4]-prices[0][4])>0:
			# 	#stock moved up due to this news
			# 	up_or_down = 1
			pos = len(prices)-20
			if (prices[pos+10][4]-prices[0][4])>0:
				#stock moved up due to this news
				up_or_down = 1
			
			if(len(text)>10):
				prediction = data_processing.relevancy_of_article(j,text,up_or_down)
			print prediction

		if(prediction == 1):
			relevant=True
		if(len(text)>20):
			table = {}
			table['text']=text
			table['img_url']=img_url
			table['title']=title
			table['url'] = url
			return_list.append(table)
		if(len(return_list)==2):
			break
	return return_list



if __name__ == '__main__':
	
	articles = getArticles("GE")
	for i in articles:
		print i['title']

	L = ["aapl","axp","ba","cat","csco","cvx","ko","dd","xom","ge","gs","hd","ibm","intc","jnj","jpm","mcd","mmm","mrk","msft","nke","pfe","pg","trv","unh","utx","v","vz","wmt","dis"]
	return_list = []
	for j in L:
		prices = stocks.getPrices(j)
		Times = [epochToEDT(x[1]) for x in prices]
		# item = epochToEDT(1490111745)
		# print item
		articles = scrap.stockQuery(j.upper())
		for i in articles:
			time = None
			text = unidecode(i['text'])
			title = i['title']
			url = i['url']
			img_url = i['img_url']
			print i['title'],i['publish_date']
			if i['publish_date'] is not None:
				time = parse_publish_date((i['publish_date']))
			else:
				print "Time not available"

			prediction = 0
			up_or_down = -1 #down
			# print str(text)
			# print i['text']
			# print data_processing.sentiment(text)
			# if(len(text)>20):
			# 	if(data_processing.sentiment(text)['Polarity']>0):
			# 		up_or_down = 1
			if(time is not None):
				pos = binSearch(Times,time)
				
				if (prices[pos+10][4]-prices[0][4])>0:
					#stock moved up due to this news
					up_or_down = 1

				if(len(text)>10):
					prediction = data_processing.relevancy_of_article(j,text,up_or_down)
				print prediction
			else:
				
				# if (prices[30][4]-prices[0][4])>0:
				# 	#stock moved up due to this news
				# 	up_or_down = 1
				pos = len(prices)-20
				if (prices[pos+10][4]-prices[0][4])>0:
					#stock moved up due to this news
					up_or_down = 1
				
				if(len(text)>10):
					prediction = data_processing.relevancy_of_article(j,text,up_or_down)
				print prediction

			if(len(text)>20):
				table = {}
				table['text']=text
				table['img_url']=img_url
				table['title']=title
				table['url'] = url
				return_list.append(table)




		
		break;

